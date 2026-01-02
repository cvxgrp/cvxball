# /// script
# dependencies = [
#     "marimo==0.18.4",
#     "matplotlib",
#     "cvxball"
# ]
#
# [tool.uv.sources]
# cvxball = { path = "../..", editable=true }
# ///

"""Interactive marimo notebook demonstrating second-order cone formulations.

This app explores multiple CVXPY formulations for the minimum enclosing ball
and visualizes their behavior on random point sets.
"""

import marimo

__generated_with = "0.11.6"
app = marimo.App()

with app.setup:
    import random

    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt
    import numpy as np

    from cvxball.solver import min_circle_cvx


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
        We are computing the smallest sphere enclosing a set of points.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## A random set of points""")
    return


@app.function
def cloud(n):
    """Generate a random cloud of 2D points.

    Args:
        n: Number of points to sample.

    Returns:
        A NumPy array of shape (n, 2) with standard normal samples.
    """
    # compute a random set of points of n_points in 2-dimensional space
    return np.array([[random.gauss(), random.gauss()] for _ in range(n)])


@app.function
def plot_points(p, p0=None, r0=None):
    """Plot 2D points and optionally overlay the enclosing circle.

    Args:
        p: Array-like collection of 2D points.
        p0: Optional center point (x, y) to draw in red.
        r0: Optional radius of the circle to draw around ``p0``.
    """
    k = len(p)

    plt.rc("savefig", dpi=120)

    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.plot([p[i][0] for i in range(k)], [p[i][1] for i in range(k)], "b*")

    if p0 is not None:
        assert r0 is not None
        ax.plot(p0[0], p0[1], "r.")
        ax.add_patch(mpatches.Circle(p0, r0, fc="w", ec="r", lw=1.5))
    plt.grid()
    plt.show()


@app.cell
def _():
    k = 500
    p = cloud(n=k)
    r0, p0 = min_circle_cvx(p, solver="CLARABEL")
    print("r0^* = ", r0)
    print("p0^* = ", p0)
    plot_points(p, p0, r0)


@app.cell
def _(mo):
    mo.md(
        r"""
        ###
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
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
