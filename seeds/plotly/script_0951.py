import plotly.express as px

fruits = ["apples", "oranges", "bananas"]
fig = px.line(x=fruits, y=[1,3,2], color=px.Constant("This year"),
             labels=dict(x="Fruit", y="Amount", color="Time Period"))
fig.add_bar(x=fruits, y=[2,1,3], name="Last year")
fig.show(renderer="json")