import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 3, 2, 4, 3, 4, 6, 5],
            mode="lines+markers",
            name="Series 1",
        ),
        go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 4, 5, 1, 2, 2, 3, 4, 2],
            mode="lines+markers",
            name="Series 2",
        ),
    ],
    layout=go.Layout(
        annotations=[
            dict(
                x=2,
                y=5,
                text="Text annotation using <b>bolded text</b>, <i>italicized text</i>, <u>underlined text</u>, <br>and a new line",
                showarrow=True,
                arrowhead=1,
            ),
            dict(
                x=4,
                y=4,
                text="Text annotation with <a href='https://dash.plotly.com'>a link</a>.",
                showarrow=False,
                yshift=10,
            ),
        ],
        showlegend=False,
    ),
)

fig.show(renderer="json")