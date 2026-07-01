import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_yaxes(autorangeoptions=dict(minallowed=3))
fig.update_xaxes(autorangeoptions=dict(maxallowed=5))

fig.show(renderer="json")