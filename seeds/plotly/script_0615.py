import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.layout.title.text = "Using Property Assignment Syntax With A Graph Object Figure"
fig.show(renderer="json")