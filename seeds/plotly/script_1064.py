import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", nbinsx=20, nbinsy=20, color_continuous_scale="Viridis")
fig.show(renderer="json")