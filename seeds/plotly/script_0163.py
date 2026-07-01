import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(range=[None, 3], autorange="max reversed")

fig.show(renderer="json")