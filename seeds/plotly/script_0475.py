import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, facet_col="medal", color=wide_df.index)
fig.show(renderer="json")