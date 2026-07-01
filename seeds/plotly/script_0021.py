import plotly.express as px
df = px.data.medals_long()

fig = px.area(df, x="medal", y="count", color="nation", pattern_shape="nation")
fig.show(renderer="json")