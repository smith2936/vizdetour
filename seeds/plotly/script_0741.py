import plotly.graph_objects as go


fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Apples", "Oranges", "Watermelon", "Pears"],
    y=[3, 2, 1, 4]
))

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    yaxis=dict(
        title=dict(
            text="Y-axis Title",
            font=dict(
                size=30
            )
        ),
        ticktext=["Very long label", "long label", "3", "label"],
        tickvals=[1, 2, 3, 4],
        tickmode="array",
    )
)

fig.update_yaxes(automargin='left+top')

fig.show(renderer="json")