import plotly.graph_objects as go

x = ['A', 'B', 'C', 'D', 'A']
y = [2, 0, 4, -3, 2]

fig = go.Figure(
    data=[
        go.Scatter(
            x=x,
            y=y,
            fill='toself',
            mode='none',
            fillcolor='lightpink'
        )
    ],
    layout=dict(
        yaxis=dict(
            zerolinelayer="above traces"  # Change to "below traces" to see the difference
        ),
    )
)

fig.show(renderer="json")