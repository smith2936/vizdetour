import plotly.graph_objects as go

fig = go.Figure(
    go.Icicle(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        root_color="lightgrey",
        textfont_size=20,
        marker=dict(pattern=dict(shape="|", size=5, solidity=0.9)),
    )
)

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show(renderer="json")