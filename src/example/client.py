import numpy as np
from loguru import logger
from np.flight import Client


def main():
    # Connect to the server
    with Client("grpc+tcp://127.0.0.1:8815") as client:
        # Example data
        # The server is expecting a dictionary of numpy arrays
        data = {"input": np.random.randn(2000, 10)}

        # The server will return a dictionary of numpy arrays
        results = client.compute(command="test", data=data)

        logger.info(f"Results: {results.keys()}")


if __name__ == "__main__":
    main()
