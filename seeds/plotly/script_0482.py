import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.scatter(mixed_df, x="experiment_1", y="experiment_2",
                color="group", facet_col="gender", hover_data=[mixed_df.index])
fig.show(renderer="json")