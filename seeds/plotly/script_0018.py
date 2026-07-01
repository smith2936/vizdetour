import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex",
    labels=dict(total_bill="Total Bill ($)", tip="Tip ($)", sex="Payer Gender")
)
fig.show(renderer="json")