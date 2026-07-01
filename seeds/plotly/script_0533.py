import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    mode = "lines+markers",
    y = [4, 1, 3],
    x = ["December", "January", "February"]))

fig.update_xaxes(
        tickangle = 90,
        title_text = "Month",
        title_font = {"size": 20},
        title_standoff = 25)

fig.update_yaxes(
        title_text = "Temperature",
        title_standoff = 25)

fig.show(renderer="json")