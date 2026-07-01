import plotly.express as px

fig = px.colors.diverging.swatches_continuous()
fig.show(renderer="json")