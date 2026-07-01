import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, countrycolor="RebeccaPurple"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show(renderer="json")