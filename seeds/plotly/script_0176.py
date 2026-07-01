import plotly.graph_objects as go

import numpy as np

np.random.seed(0)
t = np.linspace(-1, 1.2, 2000)
x = (t**3) + (0.3 * np.random.randn(2000))
y = (t**6) + (0.3 * np.random.randn(2000))

fig = go.Figure()
fig.add_trace(go.Histogram2dContour(
        x = x,
        y = y,
        colorscale = 'Blues',
        reversescale = True,
        xaxis = 'x',
        yaxis = 'y'
    ))
fig.add_trace(go.Scatter(
        x = x,
        y = y,
        xaxis = 'x',
        yaxis = 'y',
        mode = 'markers',
        marker = dict(
            color = 'rgba(0,0,0,0.3)',
            size = 3
        )
    ))
fig.add_trace(go.Histogram(
        y = y,
        xaxis = 'x2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))
fig.add_trace(go.Histogram(
        x = x,
        yaxis = 'y2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))

fig.update_layout(
    autosize = False,
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    xaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    yaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    height = 600,
    width = 600,
    bargap = 0,
    hovermode = 'closest',
    showlegend = False,
    selections = [
        dict(
            x0 = 0.5,
            x1 = -0.5,
            xref = "x",
            y0 = 190,
            y1= 0,
            yref = "y2",
            line = dict(
                color="yellow"
            )
        ),
        dict(
            x0 = -0.2,
            x1 = -1.5,
            xref = "x",
            y0 = 2,
            y1= -1,
            yref = "y",
            line = dict(
                color="yellow"
            )
        ),
        dict(
            path= "M0.75,2.39L0.98,3.38L1.46,3.68L1.80,3.35L2.01,2.51L1.67,1.15L1.18,0.50L0.65,0.66L0.54,0.83L0.49,1.56Z",
            xref= 'x',
            yref = 'y',
            line = dict(
                color='yellow'
            )
        )
    ]
)


fig.show(renderer="json")