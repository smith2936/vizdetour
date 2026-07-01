import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", facet_col="day",
                  marginal_x="box")
fig.show(renderer="json")