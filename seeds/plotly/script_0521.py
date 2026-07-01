import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_xaxes(autorangeoptions=dict(include=5))

fig.show(renderer="json")