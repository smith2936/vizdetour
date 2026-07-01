import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", marginal="rug")
fig.show(renderer="json")