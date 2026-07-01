import plotly.express as px

# List arguments
fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
fig.show(renderer="json")