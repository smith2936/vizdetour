import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="lowess", trendline_options=dict(frac=0.1))
fig.show(renderer="json")