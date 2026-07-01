import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)

fig.add_shape(
    type="rect",
    x0="2018-09-24",
    y0=0,
    x1="2018-12-18",
    y1=3,
    line_width=0,
    label=dict(text="Decline", textposition="top center", font=dict(size=20)),
    fillcolor="green",
    opacity=0.25,
)

fig.add_shape(
    type="line",
    x0=min(df.index),
    y0=1,
    x1=max(df.index),
    y1=1,
    line_width=3,
    line_dash="dot",
    label=dict(
        text="Jan 1 2018 Baseline",
        textposition="end",
        font=dict(size=20, color="blue"),
        yanchor="top",
    ),
)

fig.show(renderer="json")