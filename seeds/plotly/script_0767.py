import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(range=[None, 4.5])
fig.update_yaxes(range=[3, None])

fig.show(renderer="json")