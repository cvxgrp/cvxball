"""Convex utilities for computing the minimum enclosing circle/ball.

Provides a CVXPY-based solver for the smallest enclosing ball problem used by
tests and experiments in this repository.
"""

from typing import Any

import cvxpy as cp
import numpy as np


def min_circle_cvx(points: np.ndarray, **kwargs: dict[str, Any]) -> tuple[float, np.ndarray]:
    """Compute the smallest enclosing circle for a set of points using convex optimization.

    This function solves the convex optimization problem to find the minimum radius
    circle that contains all the given points. It uses a second-order cone constraint
    to enforce that all points lie within the circle.

    Args:
        points: A numpy array of shape (n, d) where n is the number of points
               and d is the dimension of the space.
        **kwargs: Additional keyword arguments to pass to the solver.
                 Common options include 'solver' to specify which CVXPY solver to use.

    Returns:
        A tuple containing:
            - The radius of the minimum enclosing circle (float)
            - The center coordinates of the circle (numpy.ndarray)

    Example:
        >>> import numpy as np
        >>> from cvxball.solver import min_circle_cvx
        >>> points = np.array([[0, 0], [1, 0], [0, 1]])
        >>> radius, center = min_circle_cvx(points, solver="CLARABEL")
    """
    # cvxpy variable for the radius
    r = cp.Variable(shape=1, name="Radius")
    # cvxpy variable for the midpoint
    x = cp.Variable(points.shape[1], name="Midpoint")
    objective = cp.Minimize(r)
    constraints = [
        cp.SOC(
            r * np.ones(points.shape[0]),
            points - x,  # Broadcasting handles this automatically
            axis=1,
        )
    ]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)  # type: ignore[no-untyped-call]

    # Ensure the problem was solved successfully
    assert r.value is not None, "Optimization failed to find a solution"
    assert x.value is not None, "Optimization failed to find a solution"

    return float(r.value[0]), x.value
