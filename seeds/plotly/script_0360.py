import plotly.express as px

df = px.data.stocks(indexed=True)-1
fig = px.bar(df, x=df.index, y="GOOG")
fig.update_yaxes(ticklabelposition="inside top", title=None)
fig.show(renderer="json")