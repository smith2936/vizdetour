import plotly.express as px

# List arguments in wide form
series1 = [3, 5, 4, 8]
series2 = [5, 4, 8, 3]
fig = px.line(x=[1, 2, 3, 4], y=[series1, series2])
fig.show(renderer="json")