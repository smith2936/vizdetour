import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", title="Expanding mean")
fig.show(renderer="json")