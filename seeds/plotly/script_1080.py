import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(name="first", x=["a", "b"], y=[1,2]))
fig.add_trace(go.Bar(name="second", x=["a", "b"], y=[2,1]))
fig.add_trace(go.Bar(name="third", x=["a", "b"], y=[1,2]))
fig.add_trace(go.Bar(name="fourth", x=["a", "b"], y=[2,1]))
fig.show(renderer="json")