import numpy as np
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


def serve(port=8080):
    flight_server = BallServer(host="0.0.0.0", port=port)  # nosec: B104
    print("Flight Server is listening on port 8080...")
    flight_server.run()


# entry point for Docker
if __name__ == "__main__":  # pragma: no cover
    serve(port=8080)
    # BallServer.start(host="0.0.0.0", port=8080)  # nosec: B104
