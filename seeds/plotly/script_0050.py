import plotly.express as px
df = px.data.gapminder().query("year == 2007").sort_values(by="lifeExp")
fig = px.bar(df, y="continent", x="pop", color="lifeExp", orientation="h",
             color_continuous_scale='Bluered_r', hover_name="country")

fig.show(renderer="json")