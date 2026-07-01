import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.violin(mixed_df, y=["experiment_1", "experiment_2", "experiment_3"],
                color="gender", facet_col="group", hover_data=[mixed_df.index])
fig.show(renderer="json")