import logging
import threading

import numpy as np
import pyarrow as pa
import pyarrow.flight as fl

from .solver import min_circle_cvx  # Ensure this import is correct for your environment

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_arrow_table(table):
    # Directly work with the Arrow Table (no Polars)

    logger.info(f"Handling Arrow Table: {table}")
    logger.info(f"Names: {table.schema.names}")

    matrices = {}
    for name in table.schema.names:
        logger.info(f"Name: {name}")
        struct = table.column(name)[0].as_py()

        # Extract the matrix and shape data from the Arrow Table
        matrix_data = np.array(struct["data"])  # .to_numpy()  # Flattened matrix data
        shape = np.array(struct["shape"])  # .to_numpy()  # Shape of the matrix

        logger.info(f"Matrix (flattened): {matrix_data}")
        logger.info(f"Shape: {shape}")

        if len(matrix_data) != np.prod(shape):
            raise fl.FlightServerError("Data length does not match the provided shape")

        # Reshape the flattened matrix data based on the shape
        matrix = matrix_data.reshape(shape)
        logger.info(f"Reshaped Matrix: {matrix}")

        matrices[name] = matrix

    return matrices


class BallServer(fl.FlightServerBase):
    def __init__(self, host, port):
        uri = f"grpc+tcp://{host}:{port}"
        super().__init__(uri)
        self._storage = {}  # Dictionary to store uploaded data
        self._lock = threading.Lock()  # Lock for thread safety

    def _extract_command_from_ticket(self, ticket):
        """Helper method to extract the command from a Flight Ticket."""
        return ticket.ticket.decode("utf-8")

    def do_get(self, context, ticket):
        # Get the command from the ticket
        command = self._extract_command_from_ticket(ticket)
        logger.info(f"Processing GET request for command: {command}")

        # Retrieve the stored table
        if command not in self._storage:
            raise fl.FlightServerError(f"No data found for command: {command}")

        table = self._storage[command]
        logger.info(f"Retrieved data for command: {command}")

        matrices = handle_arrow_table(table)
        matrix = matrices["input"]

        logger.info(f"Matrix: {matrix}")

        # Compute the smallest enclosing ball
        logger.info("Computing smallest enclosing ball...")
        radius, midpoint = min_circle_cvx(matrix, solver="CLARABEL")

        # Create result table
        radius_array = pa.array([radius], type=pa.float64())
        midpoint_array = pa.array([midpoint], type=pa.list_(pa.float64()))
        result_table = pa.table({"radius": radius_array, "midpoint": midpoint_array})

        logger.info("Computation completed. Returning results.")
        return fl.RecordBatchStream(result_table)
        # return result_table

    def do_put(self, context, descriptor, reader, writer):
        with self._lock:
            # Read and store the data
            command = descriptor.command.decode("utf-8")
            logger.info(f"Processing PUT request for command: {command}")

            table = reader.read_all()
            logger.info(f"Table: {table}")

            # Validate the table schema
            if "input" not in table.schema.names:
                raise fl.FlightServerError("Input column not found in the table")

            # Store the table using the command as key
            self._storage[command] = table

            logger.info(f"Data stored for command: {command}")
        return fl.FlightDescriptor.for_command(command)


def start_server():
    server = BallServer("127.0.0.1", 5006)  # Changed port to 5006
    logger.info("Starting Ball Flight server on port 5006...")
    server.serve()


if __name__ == "__main__":
    start_server()
