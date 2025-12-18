"""Unit tests for the BallServer service computing minimum enclosing balls."""

import numpy as np
import pytest

from cvx.ball.server import BallServer  # Adjust import path as needed


@pytest.fixture(scope="module")
def server():
    """Fixture providing a BallServer instance."""
    return BallServer(host="localhost", port=5008)


@pytest.fixture
def sample_points():
    """Fixture providing sample 2D points for testing."""
    return np.array([[0, 0], [1, 0], [0, 1], [1, 1]])


@pytest.fixture
def expected_ball_square(sample_points):
    """Fixture providing expected results for square points."""
    return {
        "radius": 0.7071067811865476,  # √2/2
        "midpoint": np.array([0.5, 0.5]),
        "points": sample_points,
    }


def test_initialization(server):
    """Test BallServer initialization."""
    assert isinstance(server, BallServer)
    assert server._storage == {}


def test_compute_ball_square(server, expected_ball_square):
    """Test ball computation for points forming a square."""
    # Prepare input data
    input_data = {"input": expected_ball_square["points"]}

    # Compute result
    np_dict = server.f(input_data)

    np.testing.assert_allclose(np_dict["points"], expected_ball_square["points"], atol=1e-5)
    np.testing.assert_allclose(np_dict["radius"], expected_ball_square["radius"], rtol=1e-5)
    np.testing.assert_allclose(np_dict["midpoint"], expected_ball_square["midpoint"], rtol=1e-5)


def test_invalid_input_empty(server):
    """Test handling of empty input."""
    # Empty points array
    empty_points = np.array([]).reshape(0, 2)

    # Test that it raises an appropriate error
    with pytest.raises(ValueError):  # Replace with specific exception type
        server.f({"input": empty_points})


def test_invalid_input_wrong_key(server):
    """Test handling of input with wrong dictionary key."""
    # Points with wrong dictionary key
    points = np.array([[0, 0], [1, 1]])

    with pytest.raises(KeyError):
        server.f({"wrong_key": points})
