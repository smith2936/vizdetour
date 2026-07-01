import plotly.graph_objects as go
from plotly import data

df = data.tips()

fig = go.Figure(go.Histogram2d(
        x=df.total_bill,
        y=df.tip,
        texttemplate= "%{z}"
    ))

fig.show(renderer="json")