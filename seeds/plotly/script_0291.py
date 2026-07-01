import plotly.express as px
df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')
fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='crimson', size=14))

fig.show(renderer="json")