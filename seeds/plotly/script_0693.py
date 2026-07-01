import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))

fig.update_layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes"
)
fig.update_xaxes(
    scaleanchor = "x",
    scaleratio = 1,
)
fig.update_yaxes(
    range=(-0.5, 3.5),
    constrain='domain'
)


fig.show(renderer="json")