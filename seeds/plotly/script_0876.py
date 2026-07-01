import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="yaxis data"))

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[40, 50, 60], name="yaxis2 data", yaxis="y2"))

fig.add_trace(
    go.Scatter(x=[4, 5, 6], y=[1000, 2000, 3000], name="yaxis3 data", yaxis="y3")
)

fig.add_trace(
    go.Scatter(x=[3, 4, 5], y=[400, 500, 600], name="yaxis4 data", yaxis="y4")
)


fig.update_layout(
    xaxis=dict(
        domain=[0.25, 0.75]
    ),
    yaxis=dict(
        title=dict(
            text="yaxis title"
        )
    ),
    yaxis2=dict(
        title=dict(
            text="yaxis2 title"
        ),
        overlaying="y",
        side="right"
    ),
    yaxis3=dict(
        title=dict(
            text="yaxis3 title"
        ),
        anchor="free",
        overlaying="y",
        autoshift=True
    ),
    yaxis4=dict(
        title=dict(
            text="yaxis4 title"
        ),
        anchor="free",
        overlaying="y",
        autoshift=True
    ),
)

fig.update_layout(
    title_text="Shifting y-axes with autoshift",
)

fig.show(renderer="json")