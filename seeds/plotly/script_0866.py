import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="day", color="smoker").update_xaxes(categoryorder='total descending')
fig.show(renderer="json")