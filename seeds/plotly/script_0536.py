import plotly.graph_objects as go
from plotly import data

df = data.medals_wide()

fig = go.Figure(
    data=[
        go.Bar(x=df.nation, y=df.gold, name="Gold"),
        go.Bar(x=df.nation, y=df.silver, name="Silver"),
        go.Bar(x=df.nation, y=df.bronze, name="Bronze"),
    ],
    layout=dict(
        barcornerradius=15,
    ),
)

fig.show(renderer="json")