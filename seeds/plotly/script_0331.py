import plotly.graph_objects as go
from plotly import data

df = data.gapminder()

grouped = df[df.year == 2002].loc[df[df.year == 2002].groupby('continent')['lifeExp'].idxmax()]

fig = go.Figure(
    data=go.Bar(
        x=grouped['lifeExp'],
        y=grouped['continent'],
        text=grouped['country'],
        orientation='h',
        marker_color='MediumSlateBlue',
        textfont=dict(
            lineposition="under" # combine different line positions with a "+" to add more than one: "under+over"
        )
    ),
    layout=go.Layout(
        title_text='Country with Highest Life Expectancy per Continent, 2002',
        yaxis=dict(showticklabels=False)
    )
)

fig.show(renderer="json")