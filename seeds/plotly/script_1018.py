import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a = [4, 4.5, 5, 6],
    b = [1, 2, 3],
    y = [[2, 3, 5.5, 8],
         [3.5, 4.5, 6.5, 8.5],
         [4, 5, 7.5, 10]],
    cheaterslope = -5,
    aaxis = dict(cheatertype = 'index'),
    baxis = dict(cheatertype = 'value')
))

fig.show(renderer="json")