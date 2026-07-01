import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import data

df = data.medals_wide()

fig = make_subplots(rows=1, cols=3, shared_yaxes=True)

fig.add_trace(
    go.Bar(x=df.nation, y=df.gold, name="Gold", marker=dict(cornerradius=30)), 1, 1
)
fig.add_trace(
    go.Bar(x=df.nation, y=df.silver, name="Silver", marker=dict(cornerradius="30%")),
    1,
    2,
)

fig.add_trace(
    go.Bar(x=df.nation, y=df.bronze, name="Bronze"),
    1,
    3,
)


fig.show(renderer="json")