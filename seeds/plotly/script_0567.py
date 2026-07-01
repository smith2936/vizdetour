import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_map={
             "China": ".", "Canada": "/", "South Korea": "+"
             })
fig.show(renderer="json")