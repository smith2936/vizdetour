import plotly.express as px
df = px.data.iris()
fig = px.histogram(df, x="sepal_length", color="species", marginal="box")
fig.show(renderer="json")