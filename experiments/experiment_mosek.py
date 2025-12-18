"""MOSEK Fusion experiment for the minimum enclosing ball problem.

This module compares a direct MOSEK Fusion implementation against the CVXPY
formulation for performance on random problem instances.
"""

import statistics
import timeit as tt

import mosek.fusion as mf
import numpy as np

from cvx.ball.solver import min_circle_cvx


def min_circle_mosek(points, **kwargs):
    """Solve the minimum enclosing ball using MOSEK Fusion.

    Args:
        points: Numpy array of shape (n, d) with input points.
        **kwargs: Extra keyword arguments forwarded to ``Model.solve``.

    Returns:
        A ``Circle`` containing the optimal radius and center.
    """
    with mf.Model() as model:
        r = model.variable("Radius", 1)
        x = model.variable("Midpoint", [1, points.shape[1]])

        k = points.shape[0]

        # repeat the quantities
        r0 = mf.Var.repeat(r, k)
        x0 = mf.Var.repeat(x, k)

        # https://github.com/MOSEK/Tutorials/blob/master/minimum-ellipsoid/minimum-ellipsoid.ipynb
        model.constraint(mf.Expr.hstack(r0, mf.Expr.sub(x0, points)), mf.Domain.inQCone())

        model.objective("obj", mf.ObjectiveSense.Minimize, r)
        model.solve(**kwargs)
        # Return radius and center analogous to the CVXPY API
        return r.level()[0], x.level()


if __name__ == "__main__":
    points = np.random.rand(5000, 10)

    def m1():
        """Benchmark MOSEK Fusion implementation."""
        min_circle_mosek(points)

    def m2():
        """Benchmark CVXPY formulation solved with MOSEK backend."""
        min_circle_cvx(points, solver="MOSEK")

    def m3():
        """Benchmark CVXPY formulation solved with CLARABEL backend."""
        min_circle_cvx(points, solver="CLARABEL")

    times_mosek = tt.repeat(m1, number=1, repeat=5)
    print(times_mosek)
    print(statistics.mean(times_mosek))

    times_cvx_mosek = tt.repeat(m2, number=1, repeat=5)
    print(times_cvx_mosek)
    print(statistics.mean(times_cvx_mosek))

    times_cvx_clarabel = tt.repeat(m3, number=1, repeat=5)
    print(times_cvx_clarabel)
    print(statistics.mean(times_cvx_clarabel))
