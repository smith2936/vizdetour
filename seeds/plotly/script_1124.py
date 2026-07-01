import plotly.graph_objects as go
import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/bcdunbar/datasets/master/airfoil_data.json"
data = json.load(urlopen(url))


fig=go.Figure()

fig.add_trace(go.Carpet(
    a = data[0]['a'],
    b = data[0]['b'],
    x = data[0]['x'],
    y = data[0]['y'],
    baxis = dict(
      startline = False,
      endline = False,
      showticklabels = "none",
      smoothing = 0,
      showgrid = False
    ),
    aaxis = dict(
      startlinewidth = 2,
      startline = True,
      showticklabels = "none",
      endline = True,
      showgrid = False,
      endlinewidth = 2,
      smoothing = 0
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[1]['z'],
    autocolorscale = False,
    zmax = 1,
    name = "Pressure",
    colorscale = "Viridis",
    zmin = -8,
    colorbar = dict(
      y = 0,
      yanchor = "bottom",
      len = 0.75,
      title = dict(
        text="Pressure coefficient, c<sub>p</sub>",
        side="right")
    ),
    contours = dict(
      start = -1,
      size = 0.025,
      end = 1.000,
      showlines = False
    ),
    line = dict(
      smoothing = 0
    ),
    autocontour = False,
    zauto = False
))

fig.add_trace(go.Contourcarpet(
    z = data[2]['z'],
    opacity = 0.300,
    showlegend = True,
    name = "Streamlines",
    autocontour = True,
    ncontours = 50,
    contours = dict(
      coloring = "none"
    ),
    line = dict(
      color = "white",
      width = 1
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[3]['z'],
    showlegend = True,
    name = "Pressure<br>contours",
    autocontour = False,
    line = dict(
        color = "rgba(0, 0, 0, 0.5)",
        smoothing = 1
    ),
    contours = dict(
        size = 0.250,
        start = -4,
        coloring = "none",
        end = 1.000,
        showlines = True
      )
))

fig.add_trace(go.Scatter(
    x = data[4]['x'],
    y = data[4]['y'],
    legendgroup = "g1",
    name = "Surface<br>pressure",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.5)",
      width = 1,
      shape = "spline",
      smoothing = 1
    ),
    fill = "toself",
    fillcolor = "rgba(255, 0, 0, 0.2)"
))

fig.add_trace(go.Scatter(
    x = data[5]['x'],
    y = data[5]['y'],
    showlegend = False,
    legendgroup = "g1",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.3)",
      width = 1
    )
))

fig.add_trace(go.Scatter(
    x = data[6]['x'],
    y = data[6]['y'],
    showlegend = False,
    legendgroup = "g1",
    name = "cp",
    text = data[6]['text'],
    hoverinfo = "text",
    mode = "lines",
    line = dict(
      color = "rgba(255, 0, 0, 0.2)",
      width = 0
    )
))

fig.update_layout(
    yaxis = dict(
      zeroline = False,
      range = [-1.800,1.800],
      showgrid = False
    ),
    dragmode = "pan",
    height = 700,
    xaxis = dict(
      zeroline = False,
      scaleratio = 1,
      scaleanchor = 'y',
      range = [-3.800,3.800],
      showgrid = False
    ),
    title = "Flow over a Karman-Trefftz airfoil",
    hovermode = "closest",
    margin = dict(
      r = 60,
      b = 40,
      l = 40,
      t = 80
    ),
    width = 900
)

fig.show(renderer="json")