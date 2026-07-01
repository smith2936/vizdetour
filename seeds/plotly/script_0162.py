import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(2,2)
fig.add_trace(go.Histogram2d(
    x = [ 1, 2, 2, 3, 4 ],
    y = [ 1, 2, 2, 3, 4 ],
    coloraxis = "coloraxis",
    xbins = {'start':1, 'size':1}), 1,1)
fig.add_trace(go.Histogram2d(
    x = [ 4, 5, 5, 5, 6 ],
    y = [ 4, 5, 5, 5, 6 ],
    coloraxis = "coloraxis",
    ybins = {'start': 3, 'size': 1}),1,2)
fig.add_trace(go.Histogram2d(
    x = [ 1, 2, 2, 3, 4 ],
    y = [ 1, 2, 2, 3, 4 ],
    bingroup = 1,
    coloraxis = "coloraxis",
    xbins = {'start':1, 'size':1}), 2,1)
fig.add_trace(go.Histogram2d(
    x = [ 4, 5, 5, 5, 6 ],
    y = [ 4, 5, 5, 5, 6 ],
    bingroup = 1,
    coloraxis = "coloraxis",
    ybins = {'start': 3, 'size': 1}),2,2)
fig.show(renderer="json")