import plotly.graph_objects as go

fig = go.Figure(
    [
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[3, 4, 8, 3],
            fill=None,
            mode="lines",
            line_color="darkblue",
        ),
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[1, 6, 2, 6],
            fill="tonexty",
            mode="lines",
            line_color="darkblue",
            fillgradient=dict(
                type="horizontal",
                colorscale=[(0.0, "darkblue"), (0.5, "royalblue"), (1.0, "cyan")],
            ),
        ),
    ]
)

fig.show(renderer="json")