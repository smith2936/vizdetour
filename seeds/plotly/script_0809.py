import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    center=dict(lon=-30, lat=-30),
    projection_rotation=dict(lon=30, lat=30, roll=30),
    lataxis_range=[-50,20], lonaxis_range=[0, 200]
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show(renderer="json")