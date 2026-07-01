import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'polar'}]*2]*2)

fig.add_trace(go.Scatterpolar(
        r = [1, 2, 3],
        theta = [50, 100, 200],
        marker_symbol = "square"
    ), 1, 1)
fig.add_trace(go.Scatterpolar(
        r = [1, 2, 3],
        theta = [1, 2, 3],
        thetaunit = "radians"
    ), 1, 1)
fig.add_trace(go.Scatterpolar(
        r = ["a", "b", "c", "b"],
        theta = ["D", "C", "B", "A"],
        subplot = "polar2"
    ), 1, 2)
fig.add_trace(go.Scatterpolar(
        r = [50, 300, 900],
        theta = [0, 90, 180],
        subplot = "polar3"
    ), 2, 1)
fig.add_trace(go.Scatterpolar(
        mode = "lines",
        r = [3, 3, 4, 3],
        theta = [0, 45, 90, 270],
        fill = "toself",
        subplot = "polar4"
    ), 2, 2)


fig.update_layout(
    polar = dict(
      radialaxis_range = [1, 4],
      angularaxis_thetaunit = "radians"
    ),
    polar3 = dict(
      radialaxis = dict(type = "log", tickangle = 45),
      sector = [0, 180]
    ),
    polar4 = dict(
      radialaxis = dict(visible = False, range = [0, 6])),
    showlegend = False
)

fig.show(renderer="json")