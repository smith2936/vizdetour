import plotly.graph_objects as go
from plotly import data

df = data.iris()

setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

fig = go.Figure(
    data=[
        go.Scatter(
            x=setosa_df["sepal_width"],
            y=setosa_df["sepal_length"],
            mode="markers",
            name="setosa",
        ),
        go.Scatter(
            x=versicolor_df["sepal_width"],
            y=versicolor_df["sepal_length"],
            mode="markers",
            name="versicolor",
        ),
        go.Scatter(
            x=virginica_df["sepal_width"],
            y=virginica_df["sepal_length"],
            mode="markers",
            name="virginica",
        ),
    ],
    layout=go.Layout(
        title=dict(
            text="Plot Title"
        ),
        xaxis=dict(
            title=dict(
                text="X Axis Title"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Y Axis Title"
            )
        ),
        legend=dict(
            title=dict(
                text="Legend Title"
            )
        ),
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple",
            variant="small-caps",
        )
    )
)

fig.show(renderer="json")