import plotly.graph_objects as go

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="DRAFT",
        textangle=-30,
        opacity=0.1,
        font=dict(color="black", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

fig = go.Figure()
fig.update_layout(
    template=draft_template,
    annotations=[
        dict(
            templateitemname="draft watermark",
            text="CONFIDENTIAL",
        )
    ]
)
fig.show(renderer="json")