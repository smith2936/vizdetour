import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill", color="time",
                  title="Total Bill by Sex, Colored by Time")
fig.update_layout(showlegend=False)
fig.show(renderer="json")