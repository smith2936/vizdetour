import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="Custom layout.hoverlabel formatting")
fig.update_traces(mode="markers+lines")

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)

fig.show(renderer="json")