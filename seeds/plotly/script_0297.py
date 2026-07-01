import plotly.graph_objects as go
from plotly import data

df = data.gapminder()

grouped = df[df.year == 2007].loc[df[df.year == 2007].groupby('continent')['lifeExp'].idxmax()]

fig = go.Figure(
    data=go.Bar(
        x=grouped['lifeExp'],
        y=grouped['continent'],
        text=grouped['country'],
        orientation='h',
        textfont=dict(
            family="sans serif",
            size=14,
            # Here we set textcase to "upper.
            # Set to lower" for lowercase text, or "word caps" to capitalize the first letter of each word
            textcase="upper"

        )
    ),
    layout=go.Layout(
        title_text='Country with Highest Life Expectancy per Continent, 2007',
        yaxis=dict(showticklabels=False)
    )
)

fig.show(renderer="json")