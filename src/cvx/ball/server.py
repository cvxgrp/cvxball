import numpy as np
import pyarrow as pa
import pyarrow.flight
from np.flight import Server

from cvx.ball.solver import min_circle_cvx


class BallServer(Server):
    def f(self, matrices: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
        self.logger.info(f"Matrices: {matrices.keys()}")
        matrix = matrices["input"]

        if matrix.shape[0] == 0:
            # no points were given
            raise ValueError("Matrix has no values")

        self.logger.info(f"Matrix: {matrix}")

        # Compute the smallest enclosing ball
        self.logger.info("Computing smallest enclosing ball...")
        radius, midpoint = min_circle_cvx(matrix, solver="CLARABEL")

        # return a dictionary of np.ndarrays
        return {"radius": radius, "midpoint": midpoint, "points": matrix}


class FlightServer(pyarrow.flight.FlightServerBase):
    def __init__(self, location):
        super().__init__(location)

    def do_get(self, context, ticket):
        # Handle data requests here. For now, we're just sending a sample data.
        data = pa.array([1, 2, 3, 4, 5])  # Example data
        table = pa.table({"numbers": data})
        return pyarrow.flight.RecordBatchStream(table)

    def do_put(self, context, descriptor, reader):
        # Handle receiving data. For now, we do nothing with it.
        return


def serve(port=8080):
    # Create the server instance
    location = f"grpc://0.0.0.0:{port}"
    server = FlightServer(location=location)

    # Start the server
    server.serve()
    print(f"Flight Server is listening on port {port}...")


# entry point for Docker
if __name__ == "__main__":  # pragma: no cover
    serve()
    # BallServer.start(host="0.0.0.0", port=8080)  # nosec: B104
