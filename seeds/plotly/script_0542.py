import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length",
                 color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")])

fig.show(renderer="json")