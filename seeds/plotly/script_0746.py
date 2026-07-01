import plotly.express as px

df = px.data.medals_long()

fig = px.scatter(df, y="count", x="nation", color="medal")
fig.update_traces(marker_size=10)
fig.update_layout(scattermode="group", scattergap=0.75)
fig.show(renderer="json")