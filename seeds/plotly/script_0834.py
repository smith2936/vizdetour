import plotly.graph_objects as go

y = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
     'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']

fig = go.Figure()
fig.add_trace(go.Box(
    x=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
    y=y,
    name='kale',
    marker_color='#3D9970'
))
fig.add_trace(go.Box(
    x=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
    y=y,
    name='radishes',
    marker_color='#FF4136'
))
fig.add_trace(go.Box(
    x=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
    y=y,
    name='carrots',
    marker_color='#FF851B'
))

fig.update_layout(
    xaxis=dict(title=dict(text='normalized moisture'), zeroline=False),
    boxmode='group'
)

fig.update_traces(orientation='h') # horizontal box plots
fig.show(renderer="json")