import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country",
                 log_x=True, range_x=[1,100000], range_y=[0,100])

fig.update_xaxes(minor=dict(ticks="inside", ticklen=6, showgrid=True))

fig.show(renderer="json")