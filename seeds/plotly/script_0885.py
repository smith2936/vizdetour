import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='LightGreen',
    x0=0,
    y0=0,
    x1=2,
    y1=2,
    label=dict(text="Text at 45", textangle=45),
)

fig.add_shape(
    type="rect",
    fillcolor='Gold',
    x0=3,
    y0=0,
    x1=5,
    y1=2,
    label=dict(text="Text at -45", textangle=-45),
)

fig.show(renderer="json")