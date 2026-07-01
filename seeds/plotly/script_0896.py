import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", facet_row="time",
                  marginal_y="box")
fig.show(renderer="json")