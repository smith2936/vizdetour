import plotly.express as px

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x="year", y="gdpPercap", color="country")

fig.update_layout(
    title=dict(text="GDP-per-capita", font=dict(size=50), automargin=True, yref='paper')
)

fig.show(renderer="json")