import plotly.express as px

fig = px.choropleth(
    locations=['CA', 'TX', 'NY', 'FL', 'IL'],
    locationmode='USA-states',
    color=[95, 88, 92, 85, 78],
    scope='usa',
    color_continuous_scale='Reds',
    title='USA States Choropleth'
)
fig.show(renderer="json")