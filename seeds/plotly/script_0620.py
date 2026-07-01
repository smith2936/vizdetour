import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="total_bill", y="tip", color="sex", facet_col="day",
                  marginal="box")
fig.show(renderer="json")