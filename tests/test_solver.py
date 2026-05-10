"""Tests for the convex minimum enclosing circle solver utilities."""

import numpy as np
import pytest

from cvxball.solver import min_circle_clarabel, min_circle_cvx


def test_random():
    """Validate `min_circle_cvx` on a simple 2D example with known solution."""
    p = np.array([[2.0, 4.0], [0.0, 0.0], [2.5, 2.0]])
    radius, center = min_circle_cvx(p, solver="CLARABEL")

    assert radius == pytest.approx(2.2360679626271796, 1e-6)
    assert center == pytest.approx([1.0, 2.0], 1e-4)


def test_clarabel_direct():
    """Validate `min_circle_clarabel` on a simple 2D example with known solution."""
    p = np.array([[2.0, 4.0], [0.0, 0.0], [2.5, 2.0]])
    radius, center = min_circle_clarabel(p)

    assert radius == pytest.approx(2.2360679626271796, 1e-6)
    assert center == pytest.approx([1.0, 2.0], 1e-4)


def test_clarabel_direct_matches_cvx():
    """Verify `min_circle_clarabel` and `min_circle_cvx` agree on a random instance."""
    rng = np.random.default_rng(42)
    points = rng.standard_normal((50, 5))

    radius_clarabel, center_clarabel = min_circle_clarabel(points)
    radius_cvx, center_cvx = min_circle_cvx(points, solver="CLARABEL")

    assert radius_clarabel == pytest.approx(radius_cvx, rel=1e-5)
    assert center_clarabel == pytest.approx(center_cvx, rel=1e-4)
