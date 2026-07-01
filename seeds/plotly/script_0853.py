import plotly.express as px
df = px.data.stocks(indexed=True)

fig = px.line(df, df.index, y="GOOG")
fig.update_yaxes(ticklabelposition="inside", title=dict(text="Price"))
fig.update_xaxes(insiderange=['2018-10-01', '2019-01-01'], title=dict(text="Date"))

fig.show(renderer="json")