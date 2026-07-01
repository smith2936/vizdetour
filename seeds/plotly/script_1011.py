import plotly.graph_objects as go
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 1952")

fig = go.Figure(
    data=go.Bar(x=df["country"], y=df["lifeExp"], marker_color="LightSalmon"),
    layout=dict(
        shapes=[
            dict(
                type="rect",
                x0="Germany",
                y0=0,
                x1="Germany",
                y1=0.5,
                xref="x",
                yref="paper",
                x0shift=-0.5,
                x1shift=0.5,
                line=dict(color="LightGreen", width=4),
            ),
            dict(
                type="rect",
                x0="Spain",
                y0=0,
                x1="Spain",
                y1=0.5,
                xref="x",
                yref="paper",
                x0shift=-1,
                x1shift=1,
                line=dict(color="MediumTurquoise", width=4),
            ),
        ]
    ),
)

fig.update_layout(
    title=dict(
        text="GDP per Capita in Europe (1972)"
    ),
    xaxis=dict(
        title=dict(
            text="Country"
        )
    ),
    yaxis=dict(
        title=dict(
            text="GDP per Capita"
        )
    ),
)

fig.show(renderer="json")