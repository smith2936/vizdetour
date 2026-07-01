import plotly.express as px

df = px.data.iris()

fig = px.scatter_matrix(df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species")

fig.update_layout(
    xaxis = {"matches": "y"},
    xaxis2 = {"matches": "y2"},
    xaxis3 = {"matches": "y3"},
    xaxis4 = {"matches": "y4"},
    height = 900,
    width = 750,
    dragmode = 'select',
    selections = [
        dict(
            x0 = 3,
            x1 = 4,
            xref = "x2",
            y0 = 8,
            y1= 6,
            yref = "y"
        ),
        dict(
            x0 = 5,
            x1 = 1,
            xref = "x3",
            y0 = 5,
            y1= 4,
            yref = "y",
        )
    ]
)

fig.show(renderer="json")