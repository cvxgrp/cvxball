import cvxpy as cp

from cvx.ball.utils.circle import Center, Circle


def min_circle_cvx(points, **kwargs):
    # Use con_1 if no constraint construction is defined
    # cvxpy variable for the radius
    r = cp.Variable(name="Radius")
    # cvxpy variable for the midpoint
    x = cp.Variable(points.shape[1], name="Midpoint")
    objective = cp.Minimize(r)
    constraints = [cp.SOC(r, point - x) for point in points]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)

    return Circle(radius=float(r.value), center=Center(x.value))
