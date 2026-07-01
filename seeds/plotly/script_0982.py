import plotly.express as px

fig = px.colors.cyclical.swatches_cyclical()
fig.show(renderer="json")

fig = px.colors.cyclical.swatches_continuous()
fig.show(renderer="json")