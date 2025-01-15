import numpy as np
import pytest

from cvx.ball.solver import min_circle_cvx
from cvx.ball.utils.cloud import Cloud
from cvx.ball.utils.figure import create_figure


def test_random():
    p = np.array([[2.0, 4.0], [0.0, 0.0], [2.5, 2.0]])
    circle = min_circle_cvx(p, solver="CLARABEL")

    fig = create_figure()
    fig.add_trace(circle.scatter())
    fig.add_trace(Cloud(p).scatter())

    assert circle.radius == pytest.approx(2.2360679626271796, 1e-6)
    assert circle.center.array == pytest.approx([1.0, 2.0], 1e-4)
    # fig.show()


def test_graph():
    p = np.random.randn(50, 2)
    circle = min_circle_cvx(p, solver="CLARABEL")

    fig = create_figure()
    fig.add_trace(circle.scatter())
    fig.add_trace(circle.center.scatter())
    fig.add_trace(Cloud(p).scatter(name="Cloud"))

    fig.update_layout(xaxis_range=[-3, 3], yaxis_range=[-3, 3])
    fig.show()
