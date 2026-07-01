import plotly.graph_objects as go
import plotly.data

df = plotly.data.gapminder().query("year == 2007 and continent == 'Europe'").copy()
df['gdp'] = df['gdpPercap'] * df['pop']
df = df.sort_values('gdp', ascending=False).head(4)

fig = go.Figure(
    data=[go.Bar(
        x=df['country'],
        y=df['gdp'],
        marker=dict(
            color=["lightsteelblue", "mistyrose", "palegreen", "thistle"],
            pattern=dict(
                path=[
                    "M0,0H4V4H0Z",
                    "M0,0H6V6Z",
                    "M0,0V4H4Z",
                    "M0,0C0,2,4,2,4,4C4,6,0,6,0,8H2C2,6,6,6,6,4C6,2,2,2,2,0Z"
                ],
                fgcolor=["midnightblue", "crimson", "seagreen", "indigo"],
                bgcolor=["mintcream", "lavenderblush", "azure", "honeydew"],
                size=20,
                solidity=0.7
            )
        ),
        name="GDP (2007)"
    )],
    layout=dict(
        title="Top 4 European Countries by GDP (Gapminder 2007) with Custom SVG Path Patterns",
        xaxis_title="Country",
        yaxis_title="GDP (USD)",
        yaxis_tickformat="$.2s",
        width=800,
        height=500,
        bargap=0.3
    )
)

fig.show(renderer="json")