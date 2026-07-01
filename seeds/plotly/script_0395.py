import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=dict(
            type='percent', # value of error bar given as percentage of y value
            value=50,
            visible=True)
    ))
fig.show(renderer="json")