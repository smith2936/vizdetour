import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1.5, 4.5],
    y=[0.75, 0.75],
    text=["Unfilled Rectangle", "Filled Rectangle"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 7], showgrid=False)
fig.update_yaxes(range=[0, 3.5])

# Add shapes
fig.add_shape(type="rect",
    x0=1, y0=1, x1=2, y1=3,
    line=dict(color="RoyalBlue"),
)
fig.add_shape(type="rect",
    x0=3, y0=1, x1=6, y1=2,
    line=dict(
        color="RoyalBlue",
        width=2,
    ),
    fillcolor="LightSkyBlue",
)
fig.update_shapes(dict(xref='x', yref='y'))
fig.show(renderer="json")