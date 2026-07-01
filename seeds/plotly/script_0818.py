import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True,
                 hover_name="country", hover_data=["continent", "pop"])

fig.show(renderer="json")