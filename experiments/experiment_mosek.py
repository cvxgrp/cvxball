import statistics
import timeit as tt

import mosek.fusion as mf
import numpy as np
from cvx.ball.utils.circle import Circle

from cvx.ball.solver import min_circle_cvx


def min_circle_mosek(points, **kwargs):
    with mf.Model() as M:
        r = M.variable("Radius", 1)
        x = M.variable("Midpoint", [1, points.shape[1]])

        k = points.shape[0]

        # repeat the quantities
        R0 = mf.Var.repeat(r, k)
        X0 = mf.Var.repeat(x, k)

        # https://github.com/MOSEK/Tutorials/blob/master/minimum-ellipsoid/minimum-ellipsoid.ipynb
        M.constraint(mf.Expr.hstack(R0, mf.Expr.sub(X0, points)), mf.Domain.inQCone())

        M.objective("obj", mf.ObjectiveSense.Minimize, r)
        M.solve(**kwargs)
        return Circle(radius=r.level(), center=x.level())


if __name__ == "__main__":
    points = np.random.rand(5000, 10)

    def m1():
        min_circle_mosek(points)

    def m2():
        min_circle_cvx(points, solver="MOSEK")

    def m3():
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
