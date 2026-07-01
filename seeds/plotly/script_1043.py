import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.histogram(df, x="lifeExp", color="continent", marginal="rug", hover_name="country",
                  title="Hover over the rug plot!")
fig.show(renderer="json")