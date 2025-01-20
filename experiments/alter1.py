import cvxpy as cp


def min_circle_cvx(points, **kwargs):
    # cvxpy variable for the radius
    r = cp.Variable(shape=1, name="Radius")
    # cvxpy variable for the midpoint
    x = cp.Variable(points.shape[1], name="Midpoint")
    objective = cp.Minimize(r)
    constraints = [cp.SOC(r, point - x) for point in points]

    problem = cp.Problem(objective=objective, constraints=constraints)
    problem.solve(**kwargs)

    return r.value[0], x.value
