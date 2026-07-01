import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default

fig.show(renderer="json")