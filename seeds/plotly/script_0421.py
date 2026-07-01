import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 200,
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': 400, 'relative': True, 'position' : "top"}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 350,
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 450,
    title = {"text": "Accounts<br><span style='font-size:0.8em;color:gray'>Subtitle</span><br><span style='font-size:0.8em;color:gray'>Subsubtitle</span>"},
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0.6, 1], 'y': [0, 1]}))

fig.show(renderer="json")