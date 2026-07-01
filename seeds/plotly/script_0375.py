import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    y=[3, 1, 4],
    x=["Mon", "Tue", "Wed"]))

fig.update_layout(
    title={
        'text': "Plot Title",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show(renderer="json")