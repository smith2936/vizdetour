import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, x=wide_df.index, y=wide_df.columns)
fig.show(renderer="json")