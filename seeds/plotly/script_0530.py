import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_row="smoker", facet_col="sex")
# Adds a rectangle to all facets
fig.add_shape(
    dict(type="rect", x0=25, x1=35, y0=4, y1=6, line_color="purple"),
    row="all",
    col="all",
)
# Adds a line to all the rows of the second column
fig.add_shape(
    dict(type="line", x0=20, x1=25, y0=5, y1=6, line_color="yellow"), row="all", col=2
)

# Adds a circle to all the columns of the first row
fig.add_shape(
    dict(type="circle", x0=10, y0=2, x1=20, y1=7), row=1, col="all", line_color="green"
)
fig.show(renderer="json")