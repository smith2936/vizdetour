import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df)
fig.show(renderer="json")

fig = px.area(wide_df)
fig.show(renderer="json")

fig = px.line(wide_df)
fig.show(renderer="json")

fig = px.scatter(wide_df)
fig.show(renderer="json")