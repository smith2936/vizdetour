import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=0,
    y0=0,
    x1=1.5,
    y1=1.5,
    label=dict(text="Text at middle center"),
)

fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=3,
    y0=0,
    x1=4.5,
    y1=1.5,
    label=dict(text="Text at top left", textposition="top left"),
)


fig.add_shape(
    type="line",
    line_color="MediumSlateBlue",
    x0=3,
    y0=2,
    x1=5,
    y1=3,
    line_width=3,
    label=dict(text="Text at start", textposition="start"),
)


fig.add_shape(
    type="line",
    line_color="MediumSlateBlue",
    x0=0,
    y0=2,
    x1=2,
    y1=3,
    line_width=3,
    label=dict(text="Text at middle"),
)

fig.show(renderer="json")