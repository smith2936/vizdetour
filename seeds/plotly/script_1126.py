import plotly.express as px

mixed_df = px.data.experiment(indexed=True)
wide_df = mixed_df[["experiment_1", "experiment_2", "experiment_3"]]

fig = px.histogram(wide_df)
fig.show(renderer="json")

fig = px.violin(wide_df)
fig.show(renderer="json")

fig = px.box(wide_df)
fig.show(renderer="json")