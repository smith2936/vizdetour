import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", facet_col="species")
# sources of images
sources = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Iris_setosa_var._setosa_%282595031014%29.jpg/360px-Iris_setosa_var._setosa_%282595031014%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Iris_versicolor_quebec_1.jpg/320px-Iris_versicolor_quebec_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/480px-Iris_virginica_2.jpg",
]
# add images
for col, src in enumerate(sources):
    fig.add_layout_image(
        row=1,
        col=col + 1,
        source=src,
        xref="x domain",
        yref="y domain",
        x=1,
        y=1,
        xanchor="right",
        yanchor="top",
        sizex=0.2,
        sizey=0.2,
    )

fig.show(renderer="json")