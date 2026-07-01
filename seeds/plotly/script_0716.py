import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'}]*2])

fig.add_trace(go.Scatterpolar(), 1, 1)
fig.add_trace(go.Scatterpolar(), 1, 2)

# Same data for the two Scatterpolar plots, we will only change the sector in the layout
fig.update_traces(mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line_color = "magenta",
      marker = dict(
        color = "royalblue",
        symbol = "square",
        size = 8
      ))

# The sector is [0, 360] by default, we update it for the first plot only
fig.update_layout(
    showlegend = False,
    polar = dict(# setting parameters for the second plot would be polar2=dict(...)
      sector = [150,210],
    ))


fig.show(renderer="json")