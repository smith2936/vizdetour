import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [68000, 52000, 60000, 20000, 95000, 40000, 60000, 79000, 74000, 42000, 20000, 90000]
))

fig.update_layout(
    yaxis = dict(
        showexponent = 'all',
        exponentformat = 'e'
    )
)

fig.show(renderer="json")