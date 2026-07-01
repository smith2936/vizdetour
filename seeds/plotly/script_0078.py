import plotly.express as px
import pandas as pd

df = px.data.tips()
df = df[df.day.isin(['Sat', 'Sun'])].groupby(by='day', as_index=False).sum(numeric_only=True)

fig = px.bar(df, x="day", y="total_bill")
fig.update_xaxes(labelalias=dict(Sat="Saturday", Sun="Sunday"))

fig.show(renderer="json")