import time

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from cvx.ball.solver import min_circle_cvx


def cvx(n: int) -> float:
    points = np.random.rand(n, 5)
    return min_circle_cvx(points, solver="CLARABEL")


def measure_execution_time(func, n: int, num_trials: int = 3) -> float:
    """Run multiple trials and return average execution time."""
    times = []
    for _ in range(num_trials):
        start = time.time()
        func(n)
        times.append(time.time() - start)
    return np.mean(times)


def run_analysis() -> tuple[list[int], list[float]]:
    # Test for different values of n (powers of 2)
    sequence = np.array([2**n for n in range(4, 20)])
    execution_times = []

    for n in sequence:
        avg_time = measure_execution_time(cvx, int(n))
        execution_times.append(avg_time)
        print(f"n={n}: {avg_time:.4f} seconds")

    return sequence, execution_times


def plot_results(sizes: list[int], times: list[float]) -> None:
    # Create figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add actual execution times
    fig.add_trace(
        go.Scatter(
            x=sizes, y=times, name="Actual Time", mode="lines+markers", line=dict(color="blue"), marker=dict(size=8)
        )
    )

    # Add theoretical O(n) complexity line
    normalized_n = np.array(sizes) / sizes[0]
    fig.add_trace(
        go.Scatter(x=sizes, y=normalized_n * times[0], name="O(n)", line=dict(color="red", dash="dash"), mode="lines")
    )

    # Update layout with log scales
    fig.update_layout(
        title="Algorithm Performance Analysis",
        xaxis=dict(
            title="Input Size (n)",
            type="log",
            dtick="D1",  # Show ticks for each power of 10
        ),
        yaxis=dict(title="Execution Time (seconds)", type="log", dtick="D1"),
        hovermode="x unified",
        showlegend=True,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.99),
        plot_bgcolor="white",
    )

    # Add grid lines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="LightGray")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="LightGray")

    # Show the plot
    fig.show()


if __name__ == "__main__":
    # Run the analysis
    sizes, times = run_analysis()
    plot_results(sizes, times)
