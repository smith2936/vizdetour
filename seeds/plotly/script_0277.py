import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.scatter_matrix(mixed_df, dimensions=["experiment_1", "experiment_2", "experiment_3"], color="gender")
fig.show(renderer="json")