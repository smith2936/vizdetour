import plotly.graph_objects as go

diamond_template = go.layout.Template()
diamond_template.data.scatter = [go.Scatter(marker=dict(symbol="diamond", size=20))]

fig = go.Figure()
fig.update_layout(template=diamond_template)
fig.add_scatter(y=[2, 1, 3], mode="markers")
fig.show(renderer="json")