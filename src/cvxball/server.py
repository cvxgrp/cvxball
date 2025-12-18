"""
Server implementation for computing the smallest enclosing ball for a set of points.

This module provides a server that can compute the smallest enclosing ball for a set of points
using convex optimization. It uses the min_circle_cvx function from the solver module.
"""

import numpy as np
from tschm.flight import Server

from cvxball.solver import min_circle_cvx


class BallServer(Server):
    """
    Server for computing the smallest enclosing ball for a set of points.

    This server receives a matrix of points and computes the smallest enclosing ball
    using convex optimization. It returns the radius and midpoint of the ball,
    along with the original points.

    Attributes:
        logger: A logger instance for logging information and errors.
    """

    def f(self, matrices: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
        """
        Process the input matrices and compute the smallest enclosing ball.

        Args:
            matrices: A dictionary of numpy arrays. Expected to contain an 'input' key
                     with a matrix where each row represents a point.

        Returns:
            A dictionary containing:
                - 'radius': The radius of the smallest enclosing ball (scalar)
                - 'midpoint': The center coordinates of the ball (vector)
                - 'points': The original input points (matrix)

        Raises:
            ValueError: If the input matrix is empty (has no points).
        """
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


if __name__ == "__main__":  # pragma: no cover
    BallServer.start()
