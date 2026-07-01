import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length",
                 color_continuous_scale=["red", "green", "blue"])

fig.show(renderer="json")