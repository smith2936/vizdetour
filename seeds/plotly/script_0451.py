import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", symbol="smoker", facet_col="time",
          labels={"sex": "Gender", "smoker": "Smokes"})
fig.show(renderer="json")