import pyarrow.flight as flight

client = flight.FlightClient("grpc://cvxball-710171668953.us-central1.run.app:443")
flight_info = client.get_flight_info(flight.FlightDescriptor.for_path(b"test"))
print(flight_info)
