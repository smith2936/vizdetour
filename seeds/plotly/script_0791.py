import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True, 
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Log-scaled X axis and log-transformed fit")
fig.show(renderer="json")