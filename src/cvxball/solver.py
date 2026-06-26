"""Convex utilities for computing the minimum enclosing circle/ball.

Provides two solvers for the smallest enclosing ball problem:

- :func:`min_circle_cvx`: uses CVXPY to model and then dispatch to a backend
  solver (default: CLARABEL).
- :func:`min_circle_clarabel`: bypasses CVXPY and calls the Clarabel solver
  directly, which removes the CVXPY canonicalisation overhead.
"""

from typing import Any

import clarabel
import cvxpy as cp
import numpy as np
import scipy.sparse as sp


def min_circle_cvx(points: np.ndarray, **kwargs: Any) -> tuple[float, np.ndarray]:
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
    constraints: list[cp.Constraint] = [
        cp.SOC(
            # Elementwise broadcast of the scalar radius across all points.
            # `cp.multiply` (not `*`) avoids CVXPY's deprecated `*`-as-matmul
            # path, which is ambiguous when n == 1 ((1,) * (1,) -> dot product).
            cp.multiply(r, np.ones(points.shape[0])),  # type: ignore[attr-defined]  # cvxpy re-exports atoms via star-import; stubs don't expose them
            points - x,  # Broadcasting handles this automatically
            axis=1,
        )
    ]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)  # type: ignore[no-untyped-call]  # cvxpy's Problem.solve is unannotated

    # Ensure the problem was solved successfully
    if r.value is None or x.value is None:
        raise ValueError("Optimization failed to find a solution")  # noqa: TRY003

    return float(r.value[0]), x.value


def min_circle_clarabel(points: np.ndarray, verbose: bool = False) -> tuple[float, np.ndarray]:
    """Compute the smallest enclosing circle for a set of points using Clarabel directly.

    This function solves the same convex optimisation problem as
    :func:`min_circle_cvx` but bypasses CVXPY and calls the Clarabel solver
    directly.  The problem is assembled in Clarabel's standard form::

        minimise   (1/2) z' P z + q' z
        subject to A z + s = b,  s ∈ K

    where the decision vector is ``z = [r, x₁, …, x_d]`` (radius followed by
    the d centre coordinates), the objective is to minimise *r* (so ``P = 0``,
    ``q = e₀``), and the feasible set is a product of *n* second-order cones.

    For each point ``p_i`` we require ``[r, p_i - x] in Q^{d+1}``, which gives
    one SOC block of dimension ``d + 1`` per point.

    Args:
        points: A numpy array of shape ``(n, d)`` where *n* is the number of
                points and *d* is the ambient dimension.
        verbose: If ``True``, print Clarabel's iteration log.  Defaults to
                 ``False``.

    Returns:
        A tuple ``(radius, center)`` where *radius* is the optimal enclosing
        radius (float) and *center* is a numpy array of shape ``(d,)``.

    Raises:
        ValueError: If Clarabel does not return a ``Solved`` status.

    Example:
        >>> import numpy as np
        >>> from cvxball.solver import min_circle_clarabel
        >>> points = np.array([[0, 0], [1, 0], [0, 1]])
        >>> radius, center = min_circle_clarabel(points)
    """
    n, d = points.shape
    n_vars = 1 + d  # decision vector: [r, x_1, ..., x_d]

    # --- Objective: minimise r -----------------------------------------------
    p_mat = sp.csc_matrix((n_vars, n_vars))
    q = np.zeros(n_vars)
    q[0] = 1.0

    # --- Constraints: one SOC block of size (d+1) per point ------------------
    # We need b - a_mat @ z = s  where s in K.
    # For point i the desired slack is  s = [r, p_i - x],  so:
    #   row i*(d+1)     : b = 0,       a_mat col 0   = -1  (gives s_0 = r)
    #   row i*(d+1)+j   : b = p_i[j], a_mat col j   = +1  (gives s_j = p_ij - x_j)
    total_rows = n * (d + 1)

    # Entries for the r column (column 0): -1 at each block's first row
    r_rows = np.arange(n) * (d + 1)

    # Entries for the x columns (columns 1..d): +1 at each block's inner rows
    x_row_offsets = np.arange(n)[:, None] * (d + 1) + np.arange(1, d + 1)[None, :]  # (n, d)
    x_rows = x_row_offsets.ravel()
    x_cols = np.tile(np.arange(1, d + 1), n)

    all_rows = np.concatenate([r_rows, x_rows])
    all_cols = np.concatenate([np.zeros(n, dtype=np.intp), x_cols])
    all_vals = np.concatenate([-np.ones(n), np.ones(n * d)])

    a_mat = sp.csc_matrix((all_vals, (all_rows, all_cols)), shape=(total_rows, n_vars))

    b = np.zeros(total_rows)
    b[x_rows] = points.ravel()

    # --- Cones: n SOC cones each of dimension (d+1) --------------------------
    cones = [clarabel.SecondOrderConeT(d + 1) for _ in range(n)]  # ty: ignore[unresolved-attribute]

    # --- Solve ---------------------------------------------------------------
    settings = clarabel.DefaultSettings.default()  # ty: ignore[unresolved-attribute]
    settings.verbose = verbose

    solver = clarabel.DefaultSolver(p_mat, q, a_mat, b, cones, settings)  # ty: ignore[unresolved-attribute]
    solution = solver.solve()

    if solution.status != clarabel.SolverStatus.Solved:  # ty: ignore[unresolved-attribute]
        raise ValueError(f"Clarabel did not converge: status = {solution.status}")  # noqa: TRY003

    return float(solution.x[0]), np.asarray(solution.x[1:])
