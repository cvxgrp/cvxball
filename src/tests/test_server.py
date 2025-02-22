# import pyarrow as pa
# import pyarrow.flight
# import pytest
#
# # @pytest.fixture(scope="session")
# # def flight_server():
# #    """Start the Flight server in a background thread."""
# #    server_thread = threading.Thread(target=serve, args=(8080,), daemon=True)
# #    server_thread.start()
# #    # Give the server a moment to start
# #    time.sleep(1)
# #    yield server_thread
#
#
# @pytest.fixture(scope="session")
# def flight_client():
#     """Create a Flight client connected to the test server."""
#     # return pyarrow.flight.FlightClient("grpc://hello-qz2mmrarsq-uc.a.run.app")
#     return pyarrow.flight.FlightClient("grpc+tls://cvxball-710171668953.us-central1.run.app:443")
#
#     # https://cvxball-710171668953.us-central1.run.app
#
#
# def test_do_get(flight_client):
#     """Test that the server returns the expected data."""
#     # Create a ticket
#     ticket = pyarrow.flight.Ticket(b"test")
#
#     # Get the data
#     reader = flight_client.do_get(ticket)
#     data = reader.read_all()
#
#     # Create expected data
#     expected = pa.table({"numbers": pa.array([1, 2, 3, 4, 5])})
#
#     # Verify the data
#     assert data.equals(expected)
#
#
# def test_do_put(flight_client):
#     """Test that the server can receive data without errors."""
#     # Create test data
#     test_data = pa.table({"test": pa.array([1, 2, 3])})
#
#     # Create a FlightDescriptor
#     descriptor = pyarrow.flight.FlightDescriptor.for_path(b"test")
#
#     # Put the data and verify no exceptions are raised
#     writer, _ = flight_client.do_put( descriptor, test_data.schema)
#     writer.write_table(test_data)
#     writer.close()
#
#
# @pytest.mark.parametrize(
#     "test_data",
#     [
#         pa.table({"col": pa.array([])}),  # Empty table
#         pa.table({"col": pa.array([1, 2, 3, 4, 5])}),  # Integer data
#         pa.table({"col": pa.array(["a", "b", "c"])}),  # String data
#     ],
# )
# def test_do_put_various_data(flight_client, test_data):
#     """Test that the server can handle different types of data."""
#     descriptor = pyarrow.flight.FlightDescriptor.for_path(b"test")
#     writer, _ = flight_client.do_put(descriptor, test_data.schema)
#     writer.write_table(test_data)
#     writer.close()
