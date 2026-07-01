import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color='sex', facet_row="day")
fig.update_yaxes(matches=None)
fig.show(renderer="json")