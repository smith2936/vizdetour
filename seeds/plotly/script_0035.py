import plotly.express as px
df = px.data.gapminder()
df = df.loc[(df.continent=="Asia") & (df.year==1992)]
fig = px.histogram(df, x=df.country, y=df.gdpPercap)

fig.update_xaxes(autotickangles=[45, 60, 90])

fig.show(renderer="json")