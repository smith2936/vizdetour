import plotly.graph_objects as go
from plotly import data

import pandas as pd

df = data.gapminder()
df = df.loc[(df.continent == "Europe") & (df.year.isin([1952, 2002]))]

countries = (
    df.loc[(df.continent == "Europe") & (df.year.isin([2002]))]
    .sort_values(by=["lifeExp"], ascending=True)["country"]
    .unique()
)

data = {"line_x": [], "line_y": [], "1952": [], "2002": [], "colors": [], "years": [], "countries": []}

for country in countries:
    data["1952"].extend([df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0]])
    data["2002"].extend([df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0]])
    data["line_x"].extend(
        [
            df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0],
            df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0],
            None,
        ]
    )
    data["line_y"].extend([country, country, None]),

fig = go.Figure(
    data=[
        go.Scatter(
            x=data["line_x"],
            y=data["line_y"],
            mode="lines",
            showlegend=False,
            marker=dict(
                color="grey"
            )
        ),
        go.Scatter(
            x=data["1952"],
            y=countries,
            mode="markers",
            name="1952",
            marker=dict(
                color="green",
                size=10
            )

        ),
        go.Scatter(
            x=data["2002"],
            y=countries,
            mode="markers",
            name="2002",
            marker=dict(
                color="blue",
                size=10
            )
        ),
    ]
)

fig.update_layout(
    title=dict(text="Life Expectancy in Europe: 1952 and 2002"),
    height=1000,
    legend_itemclick=False
)

fig.show(renderer="json")