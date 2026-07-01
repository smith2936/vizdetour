import plotly.graph_objects as go

fig = go.Figure([
    go.Bar(
        x=['Jan', 'Feb', 'Mar', 'Apr'],
        y=[20, 14, 25, 16],
        name='Primary Product',
        # Named CSS color
        marker_color='royalblue'
    )
])

fig.show(renderer="json")