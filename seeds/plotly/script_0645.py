import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.bar(df, x='continent', y='pop', color="lifeExp", text='country',
             title="Default behavior: some text is tiny")
fig.update_traces(textposition='inside')
fig.show(renderer="json")