import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=list(range(-5,15)),
    mode="markers",
    marker={"size": 25, "color": list(range(-3,10)), "cmid": 0}))

fig.show(renderer="json")