import plotly.express as px

fig = px.choropleth(
    locations=['USA', 'CAN', 'MEX', 'BRA', 'RUS'],
    locationmode='ISO-3',
    color=[100, 85, 72, 95, 68],
    color_continuous_scale='Viridis',
    title='Choropleth with ISO-3 Country Codes'
)
fig.show(renderer="json")