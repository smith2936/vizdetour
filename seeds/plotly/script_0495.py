import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=[1, 2, 3], y=[6, 4, 9],
                       marker_color="red")) # will be overwritten below

fig.update_traces(overwrite=True, marker={"opacity": 0.4})

fig.show(renderer="json")