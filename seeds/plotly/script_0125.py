import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    root_color="lightgrey"
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show(renderer="json")