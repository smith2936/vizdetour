import plotly.graph_objects as go

fig = go.Figure(go.Scattermap(
    name = "",
    mode = "markers+text+lines",
    lon = [-75, -80, -50],
    lat = [45, 20, -20],
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    hovertemplate =
    "<b>%{marker.symbol} </b><br><br>" +
    "longitude: %{lon}<br>" +
    "latitude: %{lat}<br>" ))

fig.update_layout(
    map = {
        'style': "outdoors", 'zoom': 1},
    showlegend = False)

fig.show(renderer="json")