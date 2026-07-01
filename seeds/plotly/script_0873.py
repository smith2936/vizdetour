import plotly.graph_objects as go

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_bar = [10, 15, 7, 10, 17, 15, 14, 20, 16, 19, 15, 17]
y_area = [12, 13, 10, 14, 15, 13, 16, 18, 15, 17, 14, 16]

area_trace = go.Scatter(
    x=x,
    y=y_area,
    fill="tozeroy",
    mode="lines+markers",
    name="Area Trace with default `zorder` of 0",
    line=dict(color="lightsteelblue"),
)

bar_trace = go.Bar(
    x=x,
    y=y_bar,
    name="Bar Trace with `zorder` of 1",
    zorder=1,
    marker=dict(color="lightslategray"),
)

fig = go.Figure(data=[area_trace, bar_trace])

fig.show(renderer="json")