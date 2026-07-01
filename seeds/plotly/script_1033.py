import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=["0", "1", "2", "3", "4", "5"],
        align="right",
    ),
    link=dict(
        arrowlen=15,
        source=[0, 1, 4, 2, 1],
        target=[1, 4, 5, 4, 3],
        value=[4, 2, 3, 1, 2]
    )
))

fig.show(renderer="json")