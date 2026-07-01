import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
))

fig.show(renderer="json")