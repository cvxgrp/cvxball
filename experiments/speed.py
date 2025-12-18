"""Micro-benchmarks comparing alternative formulations and solvers.

This script times different implementations of the minimum enclosing ball
problem on a fixed random instance.
"""

import statistics
import timeit as tt

import numpy as np

from cvx.ball.solver import min_circle_cvx
from experiments.alter1 import min_circle_cvx as alter1
from experiments.alter2 import min_circle_cvx as alter2

if __name__ == "__main__":
    points = np.random.randn(10000, 5)

    def cvx():
        """Run the CVXPY SOC vectorized formulation with CLARABEL."""
        min_circle_cvx(points, solver="CLARABEL")

    def alter_a():
        """Run the alternative SOC-per-point formulation with CLARABEL."""
        alter1(points, solver="CLARABEL")

    def alter_b():
        """Run the alternative norm-constraint formulation with CLARABEL."""
        alter2(points, solver="CLARABEL")

    times_clarabel = tt.repeat(cvx, number=1, repeat=5)
    print(times_clarabel)
    print(statistics.mean(times_clarabel))

    times_alter1 = tt.repeat(alter_a, number=1, repeat=5)
    print(times_alter1)
    print(statistics.mean(times_alter1))

    times_alter2 = tt.repeat(alter_b, number=1, repeat=5)
    print(times_alter2)
    print(statistics.mean(times_alter2))
