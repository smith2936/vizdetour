import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(tickvals=[5.1, 5.9, 6.3, 7.5])

fig.show(renderer="json")