import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill")
fig.show(renderer="json")