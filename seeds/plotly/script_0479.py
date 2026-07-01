import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x='date', y="GOOG", markers=True)
fig.add_selection(x0="2019-01-01", y0=0.95, x1="2019-10-01", y1=1.15)
fig.show(renderer="json")