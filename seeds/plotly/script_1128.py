import plotly.express as px

df = px.data.iris(return_type='polars')

fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species', size='petal_length')
fig.show(renderer="json")