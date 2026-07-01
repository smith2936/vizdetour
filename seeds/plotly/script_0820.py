import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="line",
    line_color="RoyalBlue",
    x0=3,
    y0=0,
    x1=5,
    y1=3,
    line_width=3,
    label=dict(text="Label padding of 30px", padding=30),
)

fig.add_shape(
    type="line",
    line_color="RoyalBlue",
    x0=0,
    y0=0,
    x1=2,
    y1=3,
    line_width=3,
    label=dict(text="Default label padding of 3px"),
)

fig.show(renderer="json")