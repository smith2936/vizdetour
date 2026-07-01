import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[20, 14, 23],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='hotpink',
        line=dict(color='deeppink', width=3)
    )
))
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[12, 18, 29],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='dimgray',
        line=dict(color='black', width=3)
    )
))

fig.update_layout(barmode='stack')
fig.show(renderer="json")