import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_xaxes(range=[1.5, 4.5], minallowed=1)
fig.update_yaxes(range=[3, 9], maxallowed=10)

fig.show(renderer="json")