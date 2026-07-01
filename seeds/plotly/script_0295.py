import plotly.express as px
import plotly.graph_objects as go

df = px.data.wind()
fig = px.scatter(df, y="frequency")

# Set a custom domain to see how the ' domain' string changes the behaviour
fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))

fig.add_annotation(
    xref="x domain",
    yref="y domain",
    # The arrow head will be 25% along the x axis, starting from the left
    x=0.25,
    # The arrow head will be 40% along the y axis, starting from the bottom
    y=0.4,
    text="An annotation referencing the axes",
    arrowhead=2,
)

fig.show(renderer="json")