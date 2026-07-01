import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = df.loc[(df["Date"] >= "2016-07-01") & (df["Date"] <= "2016-12-01")]

fig = px.line(df, x='Date', y='AAPL.High')
fig.update_xaxes(ticks= "outside",
                 ticklabelmode= "period",
                 tickcolor= "black",
                 ticklen=10,
                 minor=dict(
                     ticklen=4,
                     dtick=7*24*60*60*1000,
                     tick0="2016-07-03",
                     griddash='dot',
                     gridcolor='white')
                )

fig.show(renderer="json")