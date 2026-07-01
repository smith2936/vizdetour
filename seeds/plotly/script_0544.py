import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x=df.sepal_length, y=df.sepal_width, size=df.petal_length,
                 hover_data=[df.index])
fig.show(renderer="json")