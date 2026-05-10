"""Benchmark: direct Clarabel vs. CVXPY + Clarabel.

This script compares the runtime of two equivalent solvers for the minimum
enclosing ball problem on a random instance:

1. ``min_circle_clarabel`` — builds the SOCP data structures by hand and calls
   the Clarabel solver directly, avoiding any CVXPY canonicalisation overhead.
2. ``min_circle_cvx`` with ``solver="CLARABEL"`` — models the problem in CVXPY
   and lets CVXPY handle canonicalisation before dispatching to Clarabel.

Run with::

    uv run python experiments/experiment_clarabel.py
"""

import statistics
import timeit as tt

import numpy as np

from cvxball.solver import min_circle_clarabel, min_circle_cvx


def _direct(points: np.ndarray) -> None:
    """Benchmark direct Clarabel implementation."""
    min_circle_clarabel(points)


def _cvxpy(points: np.ndarray) -> None:
    """Benchmark CVXPY formulation solved with Clarabel backend."""
    min_circle_cvx(points, solver="CLARABEL")


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    points = rng.standard_normal((5000, 10))

    repeat = 5

    times_direct = tt.repeat(lambda: _direct(points), number=1, repeat=repeat)
    times_cvxpy = tt.repeat(lambda: _cvxpy(points), number=1, repeat=repeat)

    print("=== Minimum Enclosing Ball Benchmark ===")
    print(f"Problem: {points.shape[0]} points in {points.shape[1]} dimensions")
    print(f"Repeats: {repeat}\n")

    print("Direct Clarabel (no CVXPY):")
    print(f"  times  : {[round(t, 4) for t in times_direct]}")
    print(f"  mean   : {statistics.mean(times_direct):.4f} s")
    print(f"  stdev  : {statistics.stdev(times_direct):.4f} s\n")

    print("CVXPY + Clarabel:")
    print(f"  times  : {[round(t, 4) for t in times_cvxpy]}")
    print(f"  mean   : {statistics.mean(times_cvxpy):.4f} s")
    print(f"  stdev  : {statistics.stdev(times_cvxpy):.4f} s\n")

    speedup = statistics.mean(times_cvxpy) / statistics.mean(times_direct)
    print(f"Speed-up (CVXPY / direct): {speedup:.2f}x")
