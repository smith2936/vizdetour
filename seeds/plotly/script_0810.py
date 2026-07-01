import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    value = 220,
    delta = {'reference': 300},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Profit"}))
fig.update_layout(height = 250)

fig.show(renderer="json")