import plotly.graph_objects as go

fig = go.Figure()


fig.add_shape(
    type="rect",
    fillcolor="MediumSlateBlue",
    x0=-0.5,
    y0=-0.5,
    x1=1,
    y1=1,
    label=dict(
        texttemplate="x0 is %{x0:.3f}, y0 is %{y0:.3f}", font=dict(color="DarkOrange")
    ),
)

fig.add_shape(
    type="rect",
    fillcolor="LightGreen",
    x0=1,
    y0=1.75,
    x1=2.25,
    y1=3,
    label=dict(texttemplate="Height: %{height:.3f}", font=dict(color="DarkOrange")),
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=1.5,
    line_width=3,
    label=dict(
        texttemplate="Slope of %{slope:.3f} and length of %{length:.3f}",
        font=dict(size=20),
    ),
)
fig.add_shape(
    type="rect",
    fillcolor="Lavender",
    x0=2.5,
    y0=2.5,
    x1=5,
    y1=3.5,
    label=dict(
        texttemplate="Width: %{width:.3f}",
        font=dict(family="Courier New, monospace", size=20),
    ),
)

fig.show(renderer="json")