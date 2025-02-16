import numpy as np
import polars as pl
import pyarrow as pa
import pyarrow.flight as fl

from .solver import min_circle_cvx


class BallServer(fl.FlightServerBase):
    def __init__(self, host, port):
        # Bind using a valid URI format
        uri = f"grpc+tcp://{host}:{port}"
        super().__init__(uri)

    def do_get(self, context, ticket):
        # The ticket contains the matrix data as Arrow data
        table = pa.ipc.open_stream(ticket).read_all()

        # Convert Arrow Table to Polars DataFrame
        df = pl.from_arrow(table)

        # Extract the matrix data from the first row (assuming single matrix input)
        matrix_data = df[0, "data"]  # Assuming column name is 'data'
        shape = df[0, "shape"]  # Assuming shape is provided (rows, cols)

        # Convert the flattened data into a NumPy array based on shape
        matrix = np.array(matrix_data).reshape(shape)

        radius, midpoint = min_circle_cvx(matrix, solver="CLARABEL")

        # Prepare Arrow Table with the result (radius and midpoint)
        # Arrow array for radius (scalar) and midpoint (array)
        radius_array = pa.array([radius], type=pa.float64())
        midpoint_array = pa.array(midpoint, type=pa.list_(pa.float64()))

        # Create a table with the radius and midpoint
        result_table = pa.table({"radius": radius_array, "midpoint": midpoint_array})

        return fl.RecordBatchStream(result_table)

    def do_put(self, context, descriptor, reader):
        # Read the matrix data from the client
        # batch = reader.read_all()
        return fl.FlightDescriptor.for_command("Compute smallest enclosing sphere")


# Start the server
def start_server():
    server = BallServer("127.0.0.1", 5005)  # Bind to localhost and port 5005
    print("Starting Ball Flight server on port 5005...")
    server.serve()


if __name__ == "__main__":
    start_server()
