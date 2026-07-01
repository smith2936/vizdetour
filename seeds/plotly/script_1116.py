import plotly.graph_objects as go

fig = go.Figure()

# Add scatter trace for line
fig.add_trace(go.Scatter(
    x=["2015-02-01", "2015-02-02", "2015-02-03", "2015-02-04", "2015-02-05",
       "2015-02-06", "2015-02-07", "2015-02-08", "2015-02-09", "2015-02-10",
       "2015-02-11", "2015-02-12", "2015-02-13", "2015-02-14", "2015-02-15",
       "2015-02-16", "2015-02-17", "2015-02-18", "2015-02-19", "2015-02-20",
       "2015-02-21", "2015-02-22", "2015-02-23", "2015-02-24", "2015-02-25",
       "2015-02-26", "2015-02-27", "2015-02-28"],
    y=[-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
       -16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
    mode="lines",
    name="temperature"
))

# Add shape regions
fig.add_vrect(
    x0="2015-02-04", x1="2015-02-06",
    fillcolor="LightSalmon", opacity=0.5,
    layer="below", line_width=0,
),

fig.add_vrect(
    x0="2015-02-20", x1="2015-02-22",
    fillcolor="LightSalmon", opacity=0.5,
    layer="below", line_width=0,
)

fig.show(renderer="json")