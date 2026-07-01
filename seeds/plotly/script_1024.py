import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True, color='continent'
                )
print("plotly express hover template:", fig.data[0].hovertemplate)
fig.update_traces(hovertemplate='GDP: %{x} <br>Life Expectancy: %{y}') #
fig.update_traces(hovertemplate=None, selector={'name':'Europe'}) # revert to default hover
print("user defined hover template:", fig.data[0].hovertemplate)
fig.show(renderer="json")