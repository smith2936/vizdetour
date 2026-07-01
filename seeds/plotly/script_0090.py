import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", markers=True, lines=False, marginal="histogram")
fig.show(renderer="json")