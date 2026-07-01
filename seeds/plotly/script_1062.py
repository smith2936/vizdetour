import plotly.graph_objects as go
from plotly import data

df = data.gapminder()

grouped = df[df.year == 1997].loc[df[df.year == 1997].groupby('continent')['lifeExp'].idxmax()]

fig = go.Figure(
    data=go.Bar(
        x=grouped['lifeExp'],
        y=grouped['continent'],
        text=grouped['country'],
        orientation='h',
        textfont=dict(
            shadow="1px 1px 2px pink"
        )
    ),
    layout=go.Layout(
        title_text='Country with Highest Life Expectancy per Continent, 1997',
        yaxis=dict(showticklabels=False)
    )
)

fig.show(renderer="json")