import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(path="M2,6.5L4,7.5L4,6Z")

fig.show(renderer="json")