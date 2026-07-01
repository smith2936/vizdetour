import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                 labels={
                     "sepal_length": "Sepal Length (cm)",
                     "sepal_width": "Sepal Width (cm)",
                     "species": "Species of Iris"
                 },
                title="Manually Specified Labels")
fig.show(renderer="json")