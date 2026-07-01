import plotly.express as px
df = px.data.iris()

fig = px.density_contour(df, x="petal_length", y="petal_width", z="sepal_length", histfunc="avg")
fig.show(renderer="json")