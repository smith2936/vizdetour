import plotly.graph_objects as go
import plotly.data

df = plotly.data.stocks()

fig = go.Figure(
    data=[
        go.Scatter(
            x=df['date'],
            y=df['GOOG'],
            mode='lines+markers',
            name='Google Stock Price'
        )
    ],
    layout=go.Layout(
        title='Google Stock Price Over Time with Mode Bar Disabled',
        xaxis=dict(
            title='Date',
            # Try zooming in or out using the modebar buttons. These only apply to the yaxis in this example.
            modebardisable='zoominout'
        ),
        yaxis=dict(
            title='Stock Price (USD)',
        )
    )
)
fig.show(renderer="json")