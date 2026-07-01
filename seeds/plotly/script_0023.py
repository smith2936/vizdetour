import plotly.express as px
fig = px.bar(x=["Apples", "Oranges"], y=[10,20], color=["Here", "There"],
    labels=dict(x="Fruit", y="Amount", color="Place")
)
fig.show(renderer="json")