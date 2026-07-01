import plotly.express as px
df = px.data.iris()
fig = px.density_heatmap(df, x="sepal_length", y="sepal_width", marginal_x="box", marginal_y="violin")
fig.show(renderer="json")