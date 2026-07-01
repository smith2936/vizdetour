import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", y="tip", color="sex", ecdfnorm=None, orientation="h")
fig.show(renderer="json")