import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[2, 6], y=[1, 1],
    text=["Line positioned relative to the plot",
          "Line positioned relative to the axes"],
    mode="text",
))

# Set axes ranges
fig.update_xaxes(range=[0, 8])
fig.update_yaxes(range=[0, 2])

fig.add_shape(type="line",
    xref="x", yref="y",
    x0=4, y0=0, x1=8, y1=1,
    line=dict(
        color="LightSeaGreen",
        width=3,
    ),
)
fig.add_shape(type="line",
    xref="paper", yref="paper",
    x0=0, y0=0, x1=0.5,
    y1=0.5,
    line=dict(
        color="DarkOrange",
        width=3,
    ),
)

fig.show(renderer="json")