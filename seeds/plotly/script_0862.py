import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x=["total_bill", "tip"])
fig.show(renderer="json")