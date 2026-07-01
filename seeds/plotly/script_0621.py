import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='MediumSlateBlue',
    x0=1,
    y0=1,
    x1=2,
    y1=3,
    label=dict(text="Text in rectangle", font=dict(color="DarkOrange")),
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=0.8,
    line_width=3,
    label=dict(text="Text above line", font=dict(size=20)),
)
fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=2.5,
    y0=2.5,
    x1=5,
    y1=3.5,
    label=dict(
        text="Text in rectangle 2", font=dict(family="Courier New, monospace", size=20)
    ),
)

fig.show(renderer="json")