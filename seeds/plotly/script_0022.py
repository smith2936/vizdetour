import plotly.express as px
df = px.data.tips()

fig = px.violin(df, x="sex", y="total_bill", color="smoker")
fig.show(renderer="json")