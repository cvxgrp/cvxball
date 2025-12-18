"""Alternative SOC formulation for the minimum enclosing ball using CVXPY.

This module contains a simple variant of the convex program for computing the
minimum enclosing circle/ball with a second-order cone (SOC) representation.
"""

import cvxpy as cp


def min_circle_cvx(points, **kwargs):
    """Compute the minimum enclosing circle using SOC constraints via CVXPY.

    Args:
        points: Array-like of shape (n, d) with input points.
        **kwargs: Additional keyword args forwarded to ``Problem.solve``.

    Returns:
        Tuple of ``(radius, center)`` where ``radius`` is a float and
        ``center`` is an array of shape (d,).
    """
    # cvxpy variable for the radius
    r = cp.Variable(shape=1, name="Radius")
    # cvxpy variable for the midpoint
    x = cp.Variable(points.shape[1], name="Midpoint")
    objective = cp.Minimize(r)
    constraints = [cp.SOC(r, point - x) for point in points]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)

    return r.value[0], x.value
