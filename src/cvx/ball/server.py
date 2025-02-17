import numpy as np
import pyarrow as pa

from .numpy_server import NumpyServer
from .solver import min_circle_cvx


class BallServer(NumpyServer):
    def f(self, matrices: dict[str, np.ndarray]) -> pa.Table:
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
