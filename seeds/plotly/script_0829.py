import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.choropleth(
    df,
    locations='iso_alpha',
    locationmode='ISO-3',
    color='lifeExp',
    hover_name='country',
    color_continuous_scale='Viridis',
    title='Life Expectancy by Country (2007)'
)
fig.show(renderer="json")