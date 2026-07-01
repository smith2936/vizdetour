import plotly.graph_objects as go
from plotly import data

df = data.iris()

fig = go.Figure(
    [
        go.Scatter(
            x=df[df["species"] == species]["sepal_width"],
            y=df[df["species"] == species]["sepal_length"],
            mode="markers",
            name=species,
        )
        for species in df["species"].unique()
    ],
    layout=dict(
        legend=dict(
            title=dict(
                text="Species",
            ),
            indentation=10
        )
    ),
)


fig.show(renderer="json")