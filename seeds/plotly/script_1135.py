import plotly.express as px

fig = px.scatter(px.data.tips(), x="total_bill", y="tip", facet_col="smoker")
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.show(renderer="json")