import plotly.express as px

fig = px.choropleth(
    locations=['USA', 'CAN', 'GBR'],
    locationmode='ISO-3'
)
fig.show(renderer="json")