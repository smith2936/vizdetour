import plotly.express as px

df = px.data.stocks(indexed=True)

fig = px.line(df)

fig.add_shape(
    type="rect",
    x0="2018-03-01",
    y0=0,
    x1="2018-08-01",
    y1=3,
    line_width=0,
    layer="above",
    label=dict(text="Above", textposition="top center", font=dict(size=15)),
    fillcolor="LightGreen",
    opacity=0.80,
)

fig.add_shape(
    type="rect",
    x0="2018-10-01",
    y0=0,
    x1="2019-03-01",
    y1=3,
    line_width=0,
    layer="between",
    label=dict(text="Between", textposition="top center", font=dict(size=15)),
    fillcolor="LightGreen",
    opacity=0.80,
)

fig.add_shape(
    type="rect",
    x0="2019-05-01",
    y0=0,
    x1="2019-10-01",
    y1=3,
    line_width=0,
    layer="below",
    label=dict(text="Below", textposition="top center", font=dict(size=15)),
    fillcolor="LightGreen",
    opacity=0.80,
)

fig.show(renderer="json")