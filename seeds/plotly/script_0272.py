import plotly.graph_objects as go

fig = go.Figure(go.Scattermap(
    mode = "markers+text+lines",
    lon = [-75, -80, -50], lat = [45, 20, -20],
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    text = ["Bus", "Harbor", "airport"], textposition = "bottom right",
    textfont = dict(size=18, color="black", family="Open Sans Bold")
    ))

fig.update_layout(
    map = {
        'style': "outdoors", 'zoom': 0.7},
    showlegend = False,)

fig.show(renderer="json")