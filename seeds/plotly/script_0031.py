import plotly.graph_objects as go
import plotly.express as px

df = px.data.stocks()

fig = go.Figure(
    data=[
        go.Scatter(
            x=df['date'],
            y=df['GOOG'],
            mode='lines',
            name='Google'
        ),
        go.Scatter(
            x=df['date'],
            y=df['AAPL'],
            mode='lines',
            name='Apple'
        )
    ],
    layout=go.Layout(
        title_text="Stock Prices with Custom Unified Hover Title",
        hovermode='x unified',
        xaxis=dict(
            title_text='Date',
            unifiedhovertitle=dict(
                text='<b>%{x|%A, %B %d, %Y}</b>'
            )
        ),
        yaxis=dict(
            title_text='Price (USD)',
            tickprefix='$'
        )
    )
)

fig.show(renderer="json")