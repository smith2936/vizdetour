import plotly.express as px

fig = px.choropleth(
    locations=['United States', 'Canada', 'United Kingdom'],
    locationmode='country names'
)
fig.show(renderer="json")