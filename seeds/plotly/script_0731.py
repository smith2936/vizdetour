import plotly.express as px
import pandas as pd

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex")


fig.update_xaxes(minor=dict(ticklen=6, tickcolor="black", showgrid=True))
fig.update_yaxes(minor_ticks="inside")

fig.show(renderer="json")