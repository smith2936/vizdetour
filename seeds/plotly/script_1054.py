import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"],
             template="simple_white"
            )
fig.update_traces(
    marker=dict(color="black", line_color="black", pattern_fillmode="replace")
)
fig.show(renderer="json")