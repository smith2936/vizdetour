import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species", 
                 marginal_x="box", marginal_y="violin",
                  title="Click on the legend items!")
fig.show(renderer="json")