import plotly.graph_objects as go

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

fig = go.Figure()
fig.add_trace(go.Box(y=data, quartilemethod="linear", name="Linear Quartile Mode"))
fig.add_trace(go.Box(y=data, quartilemethod="inclusive", name="Inclusive Quartile Mode"))
fig.add_trace(go.Box(y=data, quartilemethod="exclusive", name="Exclusive Quartile Mode"))
fig.update_traces(boxpoints='all', jitter=0)
fig.show(renderer="json")