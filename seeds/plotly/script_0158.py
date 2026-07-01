import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(1,2)

fig.add_trace(
 go.Heatmap(x = [1, 2, 3, 4], z = [[1, 2, 3, 4], [4, -3, -1, 1]], coloraxis = "coloraxis"), 1,1)

fig.add_trace(
 go.Heatmap(x = [3, 4, 5, 6], z = [[10, 2, 1, 0], [4, 3, 5, 6]], coloraxis = "coloraxis"),1,2)
fig.update_layout(coloraxis = {'colorscale':'viridis'})

fig.show(renderer="json")