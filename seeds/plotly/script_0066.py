import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="ewm", trendline_options=dict(halflife=2),
                title="Exponentially-weighted moving average (halflife of 2 points)")
fig.show(renderer="json")