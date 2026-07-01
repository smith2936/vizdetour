import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                 values='total_bill', color='time')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show(renderer="json")