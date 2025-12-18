"""Alternative norm-based formulation for the minimum enclosing ball using CVXPY.

This variant uses explicit 2-norm constraints instead of the SOC vector form.
"""

import cvxpy as cp


def min_circle_cvx(points, **kwargs):
    """Compute the minimum enclosing circle using 2-norm constraints via CVXPY.

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
    constraints = [cp.norm2(x - point) <= r for point in points]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)

    return r.value[0], x.value
