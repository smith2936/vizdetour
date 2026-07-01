import plotly.graph_objects as go
import math

dates = [
    "2024-01-01",
    "2024-01-02",
    "2024-01-03",
    "2024-01-04",
    "2024-01-05",
    "2024-01-06",
]
y_values = [1, 30, 70, 100, 1000, 10000000]

fig = go.Figure(
    data=[go.Scatter(x=dates, y=y_values, mode="lines+markers")],
    layout=go.Layout(
        yaxis=dict(
            type="log",
        )
    ),
)

fig.add_annotation(
    x="2024-01-05",
    y=math.log10(1000),
    text="Log axis annotation",
    showarrow=True,
    xanchor="right",
)

fig.show(renderer="json")