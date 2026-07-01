import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.show(renderer="json")