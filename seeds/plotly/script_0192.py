import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")

fig.update_layout(dragmode='select',
                  newselection=dict(line=dict(color='blue')))

fig.show(renderer="json")