import plotly.express as px

fig = px.line_geo(lat=[0,15,20,35], lon=[5,10,25,30])
fig.update_geos(fitbounds="locations")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show(renderer="json")