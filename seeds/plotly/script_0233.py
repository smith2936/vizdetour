import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_white"

df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.show(renderer="json")