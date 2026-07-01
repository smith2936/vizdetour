import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, orientation="h")
fig.show(renderer="json")

fig = px.area(wide_df, x=wide_df.columns)
fig.show(renderer="json")

mixed_df = px.data.experiment(indexed=True)
wide_df = mixed_df[["experiment_1", "experiment_2", "experiment_3"]]

fig = px.histogram(wide_df, orientation="h")
fig.show(renderer="json")

fig = px.violin(wide_df, orientation="h")
fig.show(renderer="json")

fig = px.box(wide_df, orientation="h")
fig.show(renderer="json")