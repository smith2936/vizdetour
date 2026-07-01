import plotly.graph_objects as go


fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Apples", "Oranges", "Watermelon", "Pears"],
    y=[3, 2, 1, 4]
))

fig.update_layout(
    autosize=False,
    minreducedwidth=250,
    minreducedheight=250,
    width=450,
    height=450,
    yaxis=dict(
        title=dict(
            text="Y-axis Title",
            font=dict(
                size=30
            )
        ),
        ticktext=["Label", "Very long label", "Other label", "Very very long label"],
        tickvals=[1, 2, 3, 4],
        tickmode="array",
    )
)


fig.show(renderer="json")