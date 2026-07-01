import plotly.graph_objects as go
from plotly import data

df = data.gapminder()

df_germany = df.loc[(df.country.isin(["Germany"]))]
df_france = df.loc[(df.country.isin(["France"]))]
df_uk = df.loc[(df.country.isin(["United Kingdom"]))]

fig = go.Figure(
    data=[
        go.Scatter(x=df_germany.year, y=df_germany.gdpPercap, name="Germany"),
        go.Scatter(x=df_france.year, y=df_france.gdpPercap, name="France"),
        go.Scatter(x=df_uk.year, y=df_uk.gdpPercap, name="UK"),
    ],
    layout=dict(
        title=dict(text="GDP Per Capita"),
        legend={
            "x": 0.9,
            "y": 0.9,
            "xref": "container",
            "yref": "container",
            "bgcolor": "Gold",
        },
    ),
)

fig.show(renderer="json")