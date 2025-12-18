"""Approximation of π using convex optimization.

This script demonstrates how to approximate the value of π using a convex optimization approach.
It formulates a semidefinite programming (SDP) problem to find a polynomial that
under-approximates the quarter-circle, then computes the integral of this polynomial
from 0 to 1 and multiplies by 4 to get an approximation of π.

The approach uses a polynomial of the form p(x) = a + bx^2 + cx^4 and constrains it to
stay below the quarter-circle curve sqrt(1-x^2) for x in [0,1]. By maximizing the
integral of this polynomial and multiplying by 4, we get a lower bound approximation of π.

This is an example of how convex optimization can be used for numerical approximation
of mathematical constants.
"""

import cvxpy as cp
import numpy as np

if __name__ == "__main__":
    # Polynomial coefficients: p(x) = a + bx^2 + cx^4
    a = cp.Variable()
    b = cp.Variable()
    c = cp.Variable()

    # Compute integral: ∫_{0}^{1} (a + bx^2 + cx^4) dx
    integral_approx = a * 1 + b * (1 / 3) + c * (1 / 5)

    # Estimate π as 4 × integral
    pi_approx = 4 * integral_approx

    # Constraints: Ensure p(x) ≤ sqrt(1 - x^2) for x in [0,1]
    x_vals = np.linspace(0, 1, 50)  # Sampled x values for constraints
    sqrt_1_x2 = np.sqrt(1 - x_vals**2)

    constraints = [
        a + b * x_vals**2 + c * x_vals**4 <= sqrt_1_x2,  # Under-approximation
        a >= 0,  # Ensure positivity
    ]

    # Solve the SDP
    prob = cp.Problem(cp.Maximize(pi_approx), constraints)
    prob.solve(solver=cp.MOSEK)  # Use MOSEK for SDP

    print(f"Approximate π using SDP: {pi_approx.value:.6f}")
