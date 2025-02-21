import numpy as np
from loguru import logger
from np.flight import Client


def main():
    # Connect to the server
    with Client("grpc+tcp://cvxball-qz2mmrarsq-uc.a.run.app:8080") as client:
        # Example data
        # The server is expecting a dictionary of numpy arrays
        data = {"input": np.random.randn(2000, 10)}

        # The server will return a dictionary of numpy arrays
        results = client.compute(command="test", data=data)

        logger.info(f"Results: {results.keys()}")


if __name__ == "__main__":
    main()
