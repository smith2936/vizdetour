import plotly.express as px

fig = px.bar(x=["A","B","C"], y=[1,3,2])
fig.update_xaxes(showgrid=True, ticks="outside")
fig.show(renderer="json")