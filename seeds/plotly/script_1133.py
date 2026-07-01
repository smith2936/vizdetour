import plotly.express as px
import pandas as pd

df1 = pd.DataFrame(dict(time=[10, 20, 30], sales=[10, 8, 30]))
df2 = pd.DataFrame(dict(market=[4, 2, 5]))
fig = px.bar(df1, x="time", y=df2.market, color="sales")
fig.show(renderer="json")