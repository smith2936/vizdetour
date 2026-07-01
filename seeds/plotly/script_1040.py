import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False,
    resolution=50,
    showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

fig.show(renderer="json")