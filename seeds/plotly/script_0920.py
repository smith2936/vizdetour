import plotly.graph_objects as go

data = [
    go.Bar(
        x=['Q1', 'Q2', 'Q3', 'Q4'],
        y=[150, 200, 250, 300],
        name='New York',
        offsetgroup="USA"
    ),
    go.Bar(
        x=['Q1', 'Q2', 'Q3', 'Q4'],
        y=[180, 220, 270, 320],
        name='Boston',
        offsetgroup="USA"
    ),
    go.Bar(
        x=['Q1', 'Q2', 'Q3', 'Q4'],
        y=[130, 170, 210, 260],
        name='Montreal',
        offsetgroup="Canada"
    ),
    go.Bar(
        x=['Q1', 'Q2', 'Q3', 'Q4'],
        y=[160, 210, 260, 310],
        name='Toronto',
        offsetgroup="Canada"
    )
]

layout = go.Layout(
    title={
        'text': 'Quarterly Sales by City, Grouped by Country'
    },
    xaxis={
        'title': {
            'text': 'Quarter'
        }
    },
    yaxis={
        'title': {
            'text': 'Sales'
        }
    },
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)

fig.show(renderer="json")