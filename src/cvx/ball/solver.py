import cvxpy as cp
import numpy as np
from pydantic import BaseModel, Field


class ResultData(BaseModel):
    radius: float = Field(..., description="Radius of the ball", ge=0)
    midpoint: np.ndarray = Field(..., description="Midpoint of the ball")
    points: np.ndarray = Field(..., description="Points of the ball")

    class Config:
        arbitrary_types_allowed = True  # Allow numpy arrays in Pydantic
        validate_assignment = True  # Validate on attribute assignment
        frozen = True


def min_circle_cvx(points, **kwargs):
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

    # return r.value[0], x.value
    return ResultData(radius=float(r.value[0]), midpoint=x.value, points=points)
