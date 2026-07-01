import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = 220,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))

fig.show(renderer="json")