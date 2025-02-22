import pyarrow.flight as flight


def test_mini():
    # Connect to the Flight server using grpc+tls
    client = flight.FlightClient("grpc+tls://cvxball-710171668953.us-central1.run.app:443")

    # Test the connection
    try:
        flight_info = client.get_flight_info(flight.FlightDescriptor.for_path(b"test"))
        print("Connection successful!")
        print(flight_info)
    except flight.FlightUnavailableError as e:
        print("Connection failed!")
        print(e)
    except Exception as e:
        print("An error occurred:")
        print(e)
