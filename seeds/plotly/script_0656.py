import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Scatter(x=[1, 2, 3], y=[1, 2, 3], name="Trace 1"),
        go.Scatter(x=[1, 2, 3], y=[2, 3, 4], name="Trace 2"),
        go.Scatter(x=[1, 2, 3], y=[3, 4, 5], name="Trace 3", legend="legend2"),
        go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="Trace 4", legend="legend2"),
    ],
    layout=dict(
        legend=dict(
            title=dict(text="First Legend"),
            titleclick="toggleothers",
            titledoubleclick="toggle",
        ),
        legend2=dict(
            title=dict(text="Second Legend"),
            titleclick="toggleothers",
            titledoubleclick="toggle",
            y=0.5,
        ),
    ),
)

fig.show(renderer="json")