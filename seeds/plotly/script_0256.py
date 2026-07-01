import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                title="Automatic Labels Based on Data Frame Column Names")
fig.show(renderer="json")