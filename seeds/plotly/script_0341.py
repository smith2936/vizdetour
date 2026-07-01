import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(
    y=1,
    line_dash="dot",
    label=dict(
        text="Jan 1 2018 Baseline",
        textposition="end",
        font=dict(size=20, color="blue"),
        yanchor="top",
    ),
)
fig.add_vrect(
    x0="2018-09-24",
    x1="2018-12-18",
    label=dict(
        text="Decline",
        textposition="top center",
        font=dict(size=20, family="Times New Roman"),
    ),
    fillcolor="green",
    opacity=0.25,
    line_width=0,
)
fig.show(renderer="json")