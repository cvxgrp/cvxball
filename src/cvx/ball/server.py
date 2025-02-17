import pyarrow as pa
from loguru import logger

from cvx.ball.numpy_server import NumpyServer
from cvx.ball.solver import min_circle_cvx


class BallServer(NumpyServer):
    def f(self, matrices):
        self.logger.info(f"Matrices: {matrices.keys()}")
        matrix = matrices["input"]

        self.logger.info(f"Matrix: {matrix}")

        # Compute the smallest enclosing ball
        self.logger.info("Computing smallest enclosing ball...")
        radius, midpoint = min_circle_cvx(matrix, solver="CLARABEL")

        # Create result table
        radius_array = pa.array([radius], type=pa.float64())
        midpoint_array = pa.array([midpoint], type=pa.list_(pa.float64()))
        result_table = pa.table({"radius": radius_array, "midpoint": midpoint_array})
        return result_table


def start_server(port=5006):
    BallServer.start(port=port, logger=logger)  # pragma: no cover
