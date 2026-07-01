import plotly.express as px
df = px.data.tips()
fig = px.strip(df, x='day', y='tip')
fig.show(renderer="json")