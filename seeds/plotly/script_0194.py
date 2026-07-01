import plotly.express as px
import plotly.graph_objects as go

df = px.data.wind()
fig = px.scatter(df, y="frequency")

fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))
fig.add_annotation(
    xref="x domain",
    yref="y",
    x=0.75,
    y=1,
    text="An annotation whose text and arrowhead reference the axes and the data",
    # If axref is exactly the same as xref, then the text's position is
    # absolute and specified in the same coordinates as xref.
    axref="x domain",
    # The same is the case for yref and ayref, but here the coordinates are data
    # coordinates
    ayref="y",
    ax=0.5,
    ay=2,
    arrowhead=2,
)

fig.show(renderer="json")