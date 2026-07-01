import plotly.graph_objects as go

fig = go.Figure(
    go.Sunburst(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        values=[65, 14, 12, 10, 2, 6, 6, 4, 4],
        branchvalues="total",
        textfont_size=16,
        marker=dict(
            pattern=dict(
                shape=["", "/", "/", ".", ".", "/", "/", ".", "/"], solidity=0.9
            )
        ),
    )
)

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show(renderer="json")