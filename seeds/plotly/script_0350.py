import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", trendline_options=dict(function="median", window=5),
                title="Rolling Median")
fig.show(renderer="json")