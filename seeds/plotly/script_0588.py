import plotly.graph_objects as go

symbol_template = go.layout.Template()
symbol_template.data.scatter = [
    go.Scatter(marker=dict(symbol="diamond", size=10)),
    go.Scatter(marker=dict(symbol="square", size=10)),
    go.Scatter(marker=dict(symbol="circle", size=10)),
]

fig = go.Figure()
fig.update_layout(template=symbol_template)
fig.add_scatter(y=[1, 2, 3], mode="markers", name="first")
fig.add_scatter(y=[2, 3, 4], mode="markers", name="second")
fig.add_scatter(y=[3, 4, 5], mode="markers", name="third")
fig.add_scatter(y=[4, 5, 6], mode="markers", name="forth")
fig.show(renderer="json")