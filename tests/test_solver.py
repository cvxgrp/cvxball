"""Tests for the convex minimum enclosing circle solver utilities."""

from unittest.mock import MagicMock, patch

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


def test_min_circle_cvx_infeasible():
    """Raise ValueError when CVXPY returns None (infeasible/unbounded)."""
    p = np.array([[0.0, 0.0], [1.0, 1.0]])
    with (
        patch("cvxpy.Problem.solve"),
        patch("cvxpy.Variable.value", new_callable=lambda: property(lambda self: None)),
        pytest.raises(ValueError, match="Optimization failed"),
    ):
        min_circle_cvx(p)


def test_min_circle_clarabel_non_converged():
    """Raise ValueError when Clarabel returns a non-Solved status."""
    import clarabel

    p = np.array([[0.0, 0.0], [1.0, 1.0]])
    bad_solution = MagicMock()
    bad_solution.status = clarabel.SolverStatus.AlmostSolved  # ty: ignore[unresolved-attribute]

    with patch("clarabel.DefaultSolver") as mock_solver_cls:  # ty: ignore[unresolved-attribute]
        mock_solver_cls.return_value.solve.return_value = bad_solution
        with pytest.raises(ValueError, match="Clarabel did not converge"):
            min_circle_clarabel(p)
