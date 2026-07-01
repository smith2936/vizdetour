import plotly.express as px
df = px.data.tips()

fig = px.density_contour(df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")
fig.show(renderer="json")