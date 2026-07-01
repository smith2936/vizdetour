import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='turquoise',
    x0=1,
    y0=1,
    x1=2,
    y1=3,
    label=dict(text="Text in rectangle")
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=0.8,
    line_width=3,
    label=dict(text="Text above line")
)

fig.show(renderer="json")