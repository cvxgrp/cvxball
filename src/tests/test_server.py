import threading
import time

import numpy as np
import pyarrow as pa
import pyarrow.flight as fl
import pytest

from cvx.ball.server import BallServer  # Adjust to your actual import path

from .utils.reader import TableReader


@pytest.fixture(scope="module")
def server():
    """Fixture to initialize and properly kill the BallServer for each test."""
    server = BallServer("127.0.0.1", 5007)

    # Function to run the server in a separate thread
    def run_server():
        server.serve()

    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(1)

    yield server
    # Connect to the server (flight client)
    # flight_client = fl.connect("grpc+tcp://127.0.0.1:5007")

    # yield flight_client  # Provide the flight client to the test

    # After the test, ensure the server is properly cleaned up
    # flight_client.close()  # Close the client connection

    # After the test, ensure the server is properly cleaned up
    server_thread.join(timeout=5)  # Ensure the server thread has time to shutdown


@pytest.fixture(scope="module")
def client(server):
    """Fixture to initialize and properly kill the BallServer for each test."""
    # Connect to the server (flight client)
    flight_client = fl.connect("grpc+tcp://127.0.0.1:5007")

    yield flight_client  # Provide the flight client to the test

    # After the test, ensure the server is properly cleaned up
    flight_client.close()  # Close the client connection


@pytest.fixture
def mock_table():
    """Fixture to create a mock Arrow Table for tests."""
    matrix_data = [1, 2, 3, 4]  # Flattened 2x2 matrix
    shape = [2, 2]  # Shape of the matrix
    struct = {"data": matrix_data, "shape": shape}

    # Create an Arrow Table with the matrix data and shape
    table = pa.table({"input": [struct]})
    return table


@pytest.fixture
def mock_table_faulty():
    """Fixture to create a mock Arrow Table for tests."""
    matrix_data = [1, 2, 3, 4, 5, 6]  # Flattened 3x2 matrix
    shape = [2, 2]  # Shape of the matrix
    struct = {"data": matrix_data, "shape": shape}

    # Create an Arrow Table with the matrix data and shape
    table = pa.table({"input": [struct]})
    return table


def test_client(client, mock_table):
    # Simulate a 'do_put' request
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    writer, _ = client.do_put(descriptor, mock_table.schema)
    writer.write_table(mock_table)
    writer.close()

    ticket = fl.Ticket(command)  # Create a Ticket with the command
    reader = client.do_get(ticket)

    result = reader.read_all()
    assert result.column("radius")[0].as_py() == pytest.approx(1.4142135605902473)
    assert result.column("midpoint")[0].as_py() == pytest.approx(np.array([2.0, 3.0]))


def test_do_put_server(server, mock_table):
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    reader = TableReader(mock_table)

    server.do_put(None, descriptor, reader, None)


def test_do_get_server(server, mock_table):
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    # fill the storage for the correct command
    reader = TableReader(mock_table)
    server.do_put(None, descriptor, reader, None)

    # from the ticket we can extract the correct storage
    ticket = fl.Ticket(command)
    server.do_get(None, ticket)


def test_wrong_command(server, mock_table):
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    # fill the storage for the correct command
    reader = TableReader(mock_table)
    server.do_put(None, descriptor, reader, None)

    with pytest.raises(fl.FlightServerError):
        command = "Dunno"
        # from the ticket we can extract the correct storage
        ticket = fl.Ticket(command)
        server.do_get(None, ticket)


def test_faulty_data(server, mock_table_faulty):
    command = "compute_ball"
    descriptor = fl.FlightDescriptor.for_command(command)

    # fill the storage for the correct command
    reader = TableReader(mock_table_faulty)
    server.do_put(None, descriptor, reader, None)

    with pytest.raises(fl.FlightServerError):
        # from the ticket we can extract the correct storage
        ticket = fl.Ticket(command)
        server.do_get(None, ticket)
