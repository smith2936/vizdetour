import plotly.express as px

df = px.data.medals_wide(indexed=True)
fig = px.imshow(df)
fig.show(renderer="json")