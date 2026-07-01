import plotly.express as px
df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.show(renderer="json")