import numpy as np
import pytest

from cvx.ball.solver import min_circle_cvx


def test_random():
    p = np.array([[2.0, 4.0], [0.0, 0.0], [2.5, 2.0]])
    result = min_circle_cvx(p, solver="CLARABEL")

    assert result.radius == pytest.approx(2.2360679626271796, 1e-6)
    assert result.midpoint == pytest.approx([1.0, 2.0], 1e-4)
