import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", facet_row="time", facet_col="day")
fig.show(renderer="json")