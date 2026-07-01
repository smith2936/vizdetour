import plotly.express as px

df = px.data.stocks(indexed=True, datetimes=True)
fig = px.scatter(df, trendline="rolling", trendline_options=dict(window=5),
                title="5-point moving average")
fig.data = [t for t in fig.data if t.mode == "lines"]
fig.update_traces(showlegend=True) #trendlines have showlegend=False by default
fig.show(renderer="json")