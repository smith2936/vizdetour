import plotly.express as px

df = px.data.tips()
fig = px.strip(df, x="total_bill", y="time", color="sex", facet_col="day")
fig.show(renderer="json")