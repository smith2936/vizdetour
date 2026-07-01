import plotly.graph_objects as go
from plotly import data

df = data.medals_wide()

fig = go.Figure(
    data=[
        go.Bar(
            x=df.nation,
            y=df.gold,
            name="Gold",
            marker=dict(color="Gold"),
            text="Gold",
            textfont=dict(style="italic"),
        ),
        go.Bar(
            x=df.nation,
            y=df.silver,
            name="Silver",
            marker=dict(color="MediumTurquoise"),
            text="Silver",
            textfont=dict(weight="bold"),
        ),
        go.Bar(
            x=df.nation,
            y=df.bronze,
            name="Bronze",
            marker=dict(color="LightGreen"),
            text="Bronze",
            textfont=dict(variant="small-caps"),
        ),
    ],
    layout=dict(barcornerradius=15, showlegend=False),
)

fig.show(renderer="json")