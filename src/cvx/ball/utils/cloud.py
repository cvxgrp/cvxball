from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go


@dataclass(frozen=True)
class Cloud:
    points: np.ndarray

    def scatter(self, size=5, **kwargs):
        return go.Scatter(
            x=self.points[:, 0],
            y=self.points[:, 1],
            mode="markers",
            marker=dict(symbol="circle", size=size, color="black"),
            **kwargs,
        )
