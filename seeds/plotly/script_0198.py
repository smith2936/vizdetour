import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(range=[1.5, 4.5])
fig.update_yaxes(range=[3, 9])

fig.show(renderer="json")