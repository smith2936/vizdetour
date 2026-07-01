import plotly.graph_objects as go
from plotly import data

df = data.gapminder().query("continent == 'Europe' and (year == 1952 or year == 2002)")

df_pivot = df.pivot(index="country", columns="year", values="lifeExp")

fig = go.Figure(
    [
        go.Bar(
            x=df_pivot.index, y=df_pivot[1952], name="1952", marker_color="IndianRed"
        ),
        go.Bar(
            x=df_pivot.index, y=df_pivot[2002], name="2002", marker_color="LightSalmon"
        ),
    ],
    layout=dict(
        title=dict(
            text="Life Expectancy",
            subtitle=dict(
                text="Life expectancy by European country in 1952 and in 2002",
                font=dict(color="gray", size=13),
            ),
        )
    ),
)


fig.show(renderer="json")