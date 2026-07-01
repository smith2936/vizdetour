import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(
    x0=2.5, y0=6.5, x1=3.5, y1=5.5,
    line=dict(
        color="Crimson",
        width=2,
        dash="dash",
    ))

fig.show(renderer="json")