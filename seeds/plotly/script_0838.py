import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Log-transformed fit on linear axes")
fig.show(renderer="json")