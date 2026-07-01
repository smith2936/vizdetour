import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", 
                 trendline_options=dict(window=5, win_type="gaussian", function_args=dict(std=2)),
                title="Rolling Mean with Gaussian Window")
fig.show(renderer="json")