import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))
fig.update_xaxes(domain=(0.25, 0.75))
fig.update_yaxes(domain=(0.25, 0.75))
fig.show(renderer="json")