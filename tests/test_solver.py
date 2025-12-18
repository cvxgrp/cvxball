"""Tests for the convex minimum enclosing circle solver utilities."""

import numpy as np
import pytest

from cvx.ball.solver import min_circle_cvx


def test_random():
    """Validate `min_circle_cvx` on a simple 2D example with known solution."""
    p = np.array([[2.0, 4.0], [0.0, 0.0], [2.5, 2.0]])
    radius, center = min_circle_cvx(p, solver="CLARABEL")

    assert radius == pytest.approx(2.2360679626271796, 1e-6)
    assert center == pytest.approx([1.0, 2.0], 1e-4)
