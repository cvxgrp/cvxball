from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go


@dataclass(frozen=True)
class Center:
    array: np.ndarray

    def __getitem__(self, item):
        return self.array[item]

    def scatter(self, **kwargs):
        return go.Scatter(
            x=[self[0]],
            y=[self[1]],
            mode="markers",
            marker=dict(symbol="x", size=8, color="blue"),
            name=f"Center(x = {self[0]:.2f}, y = {self[1]:.2f})",
            **kwargs,
        )


@dataclass(frozen=True)
class Circle:
    center: Center
    radius: float

    def scatter(self, num=800, color="red", **kwargs):
        t = np.linspace(0, 2 * np.pi, num=num)
        radius = self.radius
        circle_x = self.center[0] + radius * np.cos(t)
        circle_y = self.center[1] + radius * np.sin(t)

        return go.Scatter(
            x=circle_x,
            y=circle_y,
            mode="lines",
            line=dict(color=color, width=1),
            name=f"Circle(r = {self.radius:.2f})",
            **kwargs,
        )
