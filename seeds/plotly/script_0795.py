import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(x=["a","b"], y=[1,2], marker_pattern_shape="."))
fig.add_trace(go.Bar(x=["a","b"], y=[3,1], marker_pattern_shape="x"))
fig.add_trace(go.Bar(x=["a","b"], y=[2,3], marker_pattern_shape="+"))

fig.show(renderer="json")