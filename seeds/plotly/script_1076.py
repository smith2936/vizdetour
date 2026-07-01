import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", y="tip", color="sex", ecdfnorm=None)
fig.show(renderer="json")