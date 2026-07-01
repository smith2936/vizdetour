import plotly.graph_objects as go

fig = go.Figure(
    go.Treemap(
        labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        root_color="lightgrey",
        textfont_size=20,
        marker=dict(pattern=dict(shape=["|"], solidity=0.80)),
    )
)

fig.show(renderer="json")