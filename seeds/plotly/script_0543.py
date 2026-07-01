import plotly.graph_objects as go

labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
values = [4500, 2500, 1053, 500]
colors = ["gold", "mediumturquoise", "darkorange", "lightgreen"]

fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            textfont_size=20,
            marker=dict(colors=colors, pattern=dict(shape=[".", "x", "+", "-"]))
        )
    ]
)

fig.show(renderer="json")