import plotly.express as px

fig = px.choropleth(
    locations=['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    locationmode='USA-states',
    color=[95, 88, 92, 85, 78],
    scope='usa',
    color_continuous_scale='Reds',
    title='USA States Choropleth with State Names'
)
fig.show(renderer="json")