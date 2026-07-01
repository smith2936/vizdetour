import plotly.graph_objects as go
import plotly.express as px

df = px.data.wind()
fig = px.scatter(df, y="frequency")

fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))

# Add a shape whose x and y coordinates refer to the domains of the x and y axes
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=0.6, x1=0.7, y0=0.8, y1=0.9,
)

fig.show(renderer="json")