import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.bar(df, x='continent', y='pop', color="lifeExp", text='country',
             title="Uniform Text: min size is 8, hidden if can't fit")
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show(renderer="json")