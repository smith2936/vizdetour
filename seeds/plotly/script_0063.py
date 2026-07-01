import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="day").update_xaxes(categoryorder='total ascending')
fig.show(renderer="json")