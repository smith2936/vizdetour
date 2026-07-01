import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", trendline_options=dict(function="max"),
                title="Expanding Maximum")
fig.show(renderer="json")