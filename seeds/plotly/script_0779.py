import plotly.graph_objects as go
import pandas as pd
from plotly import data

df = data.stocks()

layout = dict(
    hoversubplots="axis",
    title=dict(text="Stock Price Changes"),
    hovermode="x",
    grid=dict(rows=3, columns=1),
)

data = [
    go.Scatter(x=df["date"], y=df["AAPL"], xaxis="x", yaxis="y", name="Apple"),
    go.Scatter(x=df["date"], y=df["GOOG"], xaxis="x", yaxis="y2", name="Google"),
    go.Scatter(x=df["date"], y=df["AMZN"], xaxis="x", yaxis="y3", name="Amazon"),
]

fig = go.Figure(data=data, layout=layout)

fig.show(renderer="json")