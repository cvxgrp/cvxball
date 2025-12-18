from typing import Any, Dict, Tuple

import cvxpy as cp
import numpy as np


def min_circle_cvx(points: np.ndarray, **kwargs: Dict[str, Any]) -> Tuple[float, np.ndarray]:
    """
    Compute the smallest enclosing circle for a set of points using convex optimization.

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
            points - cp.outer(np.ones(points.shape[0]), x),
            axis=1,
        )
    ]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)

    return r.value[0], x.value
