import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="day", y="total_bill", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))
fig.show(renderer="json")