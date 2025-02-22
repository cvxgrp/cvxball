import numpy as np
from np.flight import Client


def main():
    # Connect to the server
    with Client("grpc+tls://cvxball-710171668953.us-central1.run.app:443") as client:
        # Example data
        # The server is expecting a dictionary of numpy arrays
        data = {"input": np.random.randn(2000, 10)}

        # The server will return a dictionary of numpy arrays
        results = client.compute(command="test", data=data)

        # logger.info(f"Results: {results.keys()}")
        print("Hello World!")
        print(results)
        pass


if __name__ == "__main__":
    # Connect to server and do computation
    main()
