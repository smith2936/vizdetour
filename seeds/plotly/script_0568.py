import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=['A', 'B', 'C', 'D', 'E', 'F'],
        x=[0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
        y=[0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
        pad=10,
        align="right",
    ),
    link=dict(
        arrowlen=15,
        source=[0, 0, 1, 2, 5, 4, 3, 5],
        target=[5, 3, 4, 3, 0, 2, 2, 3],
        value=[1, 2, 1, 1, 1, 1, 1, 2]
    )
))

fig.show(renderer="json")