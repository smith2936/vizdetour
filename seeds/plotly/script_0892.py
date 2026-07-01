import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
      tickprefix = 'a = ',
      ticksuffix = 'm',
      smoothing = 1,
      minorgridcount = 9
      ),
    baxis = dict(
      tickprefix = 'b = ',
      ticksuffix = 'Pa',
      smoothing = 1,
      minorgridcount = 9
      )
))

fig.add_trace(go.Scattercarpet(
    a = [4, 4.5, 5, 6],
    b = [2.5, 2.5, 2.5, 2.5],
    line = dict(
      shape = 'spline',
      smoothing = 1,
      color = 'blue'
    )
))

fig.show(renderer="json")