import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.box(mixed_df, x="group", y=["experiment_1", "experiment_2", "experiment_3"],
                color="gender", facet_col="variable", hover_data=[mixed_df.index])
fig.show(renderer="json")