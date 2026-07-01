import plotly.express as px
wide_df = px.data.medals_wide(indexed=False)

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], facet_col="variable", color="nation")
fig.show(renderer="json")