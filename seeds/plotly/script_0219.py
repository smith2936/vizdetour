import plotly.express as px
from plotly import data

df = data.gapminder().query("year==2007 and continent == 'Europe'")

fig = px.scatter(df,
                 x="gdpPercap",
                 y="lifeExp",
                 color="country",
                 size="pop",
                 size_max=45,
                 title="Life Expectancy vs. GDP per Capita in 2007 (by Country)",
                 labels={"gdpPercap": "GDP per Capita"},
                )

fig.update_layout(
    xaxis=dict(
        side="top"
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="center",
        x=0.5,
        maxheight=0.1, # Comment maxheight to see legend take up 0.5 of plotting area
        title_text="Country"
    ),
)

fig.show(renderer="json")