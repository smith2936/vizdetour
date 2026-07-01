import pandas as pd
import plotly.graph_objects as go
from plotly import data

df = data.gapminder()
df = df.loc[(df.continent == "Americas") & (df.year.isin([1987, 2007]))]

countries = (
    df.loc[(df.continent == "Americas") & (df.year.isin([2007]))]
    .sort_values(by=["pop"], ascending=True)["country"]
    .unique()
)[5:-10]

data = {"x": [], "y": [], "colors": [], "years": []}

for country in countries:
    data["x"].extend(
        [
            df.loc[(df.year == 1987) & (df.country == country)]["pop"].values[0],
            df.loc[(df.year == 2007) & (df.country == country)]["pop"].values[0],
            None,
        ]
    )
    data["y"].extend([country, country, None]),
    data["colors"].extend(["cyan", "darkblue", "white"]),
    data["years"].extend(["1987", "2007", None])

fig = go.Figure(
    data=[
        go.Scatter(
            x=data["x"],
            y=data["y"],
            mode="markers+lines",
            marker=dict(
                symbol="arrow",
                color="royalblue",
                size=16,
                angleref="previous",
                standoff=8,
            ),
        ),
        go.Scatter(
            x=data["x"],
            y=data["y"],
            text=data["years"],
            mode="markers",
            marker=dict(
                color=data["colors"],
                size=16,
            ),
            hovertemplate="""Country: %{y} <br> Population: %{x} <br> Year: %{text} <br><extra></extra>""",
        ),
    ]
)

fig.update_layout(
    title=dict(text="Population changes 1987 to 2007"),
    width=1000,
    height=1000,
    showlegend=False,
)


fig.show(renderer="json")