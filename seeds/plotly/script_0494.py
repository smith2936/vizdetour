import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_yaxes(autorangeoptions=dict(clipmin=5))
fig.update_xaxes(autorangeoptions=dict(clipmax=4))

fig.show(renderer="json")