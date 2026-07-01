import plotly.express as px

df = px.data.tips()
fig = px.parallel_categories(df)

fig.show(renderer="json")