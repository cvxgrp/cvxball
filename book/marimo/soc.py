# /// script
# dependencies = [
#     "marimo==0.18.4",
#     "numpy==2.3.1",
#     "matplotlib",
#     "cvxpy-base",
#     "clarabel",
# ]
# ///

"""Interactive marimo notebook demonstrating second-order cone formulations.

This app explores multiple CVXPY formulations for the minimum enclosing ball
and visualizes their behavior on random point sets.
"""

import marimo

__generated_with = "0.11.6"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""# Second order cones""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        cvxpy supports second order cones, see:
        https://www.cvxpy.org/examples/basic/socp.html
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""The discussion in this notebook follows https://github.com/MOSEK/Tutorials/blob/master/minimum-ellipsoid/minimum-ellipsoid.ipynb"""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        We are computing the smallest sphere enclosing a set of points. We are introducing
        three mildly different implementations of this problem all based on cvxpy. However,
        the freedom to render problems can result in somewhat poor choices.
        Here we demonstrate the incredible potential of second order cones on a classic problem.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## A random set of points""")
    return


@app.cell
def _():
    import random

    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt
    import numpy as np

    def plot_points(p, p0=[], r0=0.0):
        k = len(p)

        plt.rc("savefig", dpi=120)

        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        ax.plot([p[i][0] for i in range(k)], [p[i][1] for i in range(k)], "b*")

        if len(p0) > 0:
            ax.plot(p0[0], p0[1], "r.")
            ax.add_patch(mpatches.Circle(p0, r0, fc="w", ec="r", lw=1.5))
        plt.grid()
        plt.show()

    n = 2
    k = 500

    p = np.array([[random.gauss(0.0, 10.0) for nn in range(n)] for kk in range(k)])

    plot_points(p)
    return k, mpatches, n, np, p, plot_points, plt, random


@app.cell
def _(mo):
    mo.md(
        r"""
        ## The problem

        The problem boils down to determine the sphere center $p_0\in \mathbb{R}^n$
        and its radius $r_0\geq 0$, i.e.


        \begin{equation}
          \begin{aligned}
        \min \max_{i=1,\dots,k} \| p_0 - p_i\|_2 \\
          \end{aligned}
        \end{equation}

        The maximum in the objective function can be easily, i.e.

        \begin{equation}
          \begin{aligned}
        \min r_0 & & &\\
        s.t.& & &\\
        & r_0 \geq \| p_0 - p_i\|_2 ,& \quad & i=1,\ldots,k\\
        \end{aligned}
        \end{equation}

        The SOCP formulation reads

        \begin{equation}
          \begin{aligned}
        \min r_0 & & &\\
        s.t.& & &\\
        & \left[r_0,p_0 - p_i\right] \in Q^{(n+1)}, & \quad & i=1,\ldots,k.
        \end{aligned}
        \end{equation}

        where $Q^{(n+1)} = \left\{ (t,x) ∈ \mathbb{R} \times \mathbb{R}^n : \|x\|_2  \leq t \right\}$
        is the $(n+1)$ dimensional second-order cone.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### With n constraints: Distance from center for each point

        Unaware of cones we could write this problem as
        """
    )
    return


@app.cell
def _():
    import cvxpy as cp

    def min_circle_cvx_norm(points, **kwargs):
        # cvxpy variable for the radius
        r = cp.Variable(shape=1, name="Radius")
        # cvxpy variable for the midpoint
        x = cp.Variable(points.shape[1], name="Midpoint")
        objective = cp.Minimize(r)
        constraints = [cp.norm2(x - point) <= r for point in points]

        problem = cp.Problem(objective=objective, constraints=constraints)
        problem.solve(**kwargs)

        return r.value[0], x.value

    return cp, min_circle_cvx_norm


@app.cell
def _(min_circle_cvx_norm, p):
    r0, p0 = min_circle_cvx_norm(p, solver="CLARABEL")
    print("r0^* = ", r0)
    print("p0^* = ", p0)
    return p0, r0


@app.cell
def _(p, p0, plot_points, r0):
    plot_points(p, p0, r0)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### With n constraints: One second-order cone for each point

        Using cones we can replace each individual constraint with a cone.
        This syntactic sugar will reduce the runtime
        """
    )
    return


@app.cell
def _(cp):
    def min_circle_cvx_socs(points, **kwargs):
        # cvxpy variable for the radius
        r = cp.Variable(shape=1, name="Radius")
        # cvxpy variable for the midpoint
        x = cp.Variable(points.shape[1], name="Midpoint")
        objective = cp.Minimize(r)
        constraints = [cp.SOC(r, point - x) for point in points]

        problem = cp.Problem(objective=objective, constraints=constraints)
        problem.solve(**kwargs)

        return r.value[0], x.value

    return (min_circle_cvx_socs,)


@app.cell
def _(min_circle_cvx_socs, p):
    r0_1, p0_1 = min_circle_cvx_socs(p, solver="CLARABEL")
    print("r0^* = ", r0_1)
    print("p0^* = ", p0_1)
    return p0_1, r0_1


@app.cell
def _(p, p0_1, plot_points, r0_1):
    plot_points(p, p0_1, r0_1)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### With one constraint: Getting rid of loop

        We follow Mosek's excellent documentation:

        Before defining the constraints, we note that we can write

        \begin{equation}
        R_0 = \left( \begin{array}{c} r_0   \\ \vdots \\ r_0   \end{array} \right) \in \mathbb{R}^k          , \quad
        P_0 = \left( \begin{array}{c} p_0^T \\ \vdots \\ p_0^T \end{array} \right) \in \mathbb{R}^{k\times n}, \quad
        P   = \left( \begin{array}{c} p_1^T \\ \vdots \\ p_k^T \end{array} \right) \in \mathbb{R}^{k\times n}.
        \end{equation}

        so that

        \begin{equation}
        \left[r_0,p_i - p_0\right] \in Q^{(n+1)},  \quad  i=1,\ldots,k.
        \end{equation}

        can be compactly expressed as

        \begin{equation}
        \left[ R_0,P_0-P\right] \in \Pi Q^{(n+1)},
        \end{equation}

        that means, with a little abuse of notation, that each rows belongs to a
        quadratic cone of dimension $n+1$.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        We can take over the idea for cvxpy and can get away with a single call of 'cp.SOC'.
        The loop has disappeared into matrix algebra which is in general a good idea
        when using Python.
        """
    )
    return


@app.cell
def _(cp, np):
    def min_circle_cvx_soc(points, **kwargs):
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

    return (min_circle_cvx_soc,)


@app.cell
def _(min_circle_cvx_soc, p):
    r0_2, p0_2 = min_circle_cvx_soc(p, solver="CLARABEL")
    print("r0^* = ", r0_2)
    print("p0^* = ", p0_2)
    return p0_2, r0_2


@app.cell
def _(p, p0_2, plot_points, r0_2):
    plot_points(p, p0_2, r0_2)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Benchmark

        We have demonstrated that all implementation above give the same results.
        So why bother?

        Using a more junky set of points we compare their runtime and
        reveal huge differences:
        """
    )
    return


@app.cell
def _(np):
    p_1 = np.random.randn(10000, 5)
    return (p_1,)


@app.cell
def _(min_circle_cvx_norm, p_1):
    min_circle_cvx_norm(p_1, solver="CLARABEL")
    return


@app.cell
def _(min_circle_cvx_socs, p_1):
    min_circle_cvx_socs(p_1, solver="CLARABEL")
    return


@app.cell
def _(min_circle_cvx_soc, p_1):
    min_circle_cvx_soc(p_1, solver="CLARABEL")
    return


@app.cell
def _(mo):
    mo.md(r"""## Summary""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Avoiding the loop explicitly constructing a second-order cone for each
        point leads to dramatic speed-ups.
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
