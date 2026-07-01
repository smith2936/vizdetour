import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[1.5, 3.5],
    y=[0.75, 2.5],
    text=["Unfilled Circle",
          "Filled Circle"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 4.5], zeroline=False)
fig.update_yaxes(range=[0, 4.5])

# Add circles
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=1, y0=1, x1=3, y1=3,
    line_color="LightSeaGreen",
)
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="PaleTurquoise",
    x0=3, y0=3, x1=4, y1=4,
    line_color="LightSeaGreen",
)

# Set figure size
fig.update_layout(width=800, height=800)

fig.show(renderer="json")