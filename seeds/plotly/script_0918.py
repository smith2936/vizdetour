import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    name="Name of Trace 1"       # this sets its legend entry
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
    name="Name of Trace 2"
))

fig.update_layout(
    title=dict(
        text="Plot Title"
    ),
    xaxis=dict(
        title=dict(
            text="X Axis Title"
        )
    ),
    yaxis=dict(
        title=dict(
            text="Y Axis Title"
        )
    ),
    legend=dict(
        title=dict(
            text="Legend Title"
        )
    ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show(renderer="json")