import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1,2,3,4,5],
    y = [2.02825,1.63728,6.83839,4.8485,4.73463],
    hovertemplate =
    '<i>Price</i>: $%{y:.2f}'+
    '<br><b>X</b>: %{x}<br>'+
    '<b>%{text}</b>',
    text = ['Custom text {}'.format(i + 1) for i in range(5)],
    showlegend = False))

fig.add_trace(go.Scatter(
    x = [1,2,3,4,5],
    y = [3.02825,2.63728,4.83839,3.8485,1.73463],
    hovertemplate = 'Price: %{y:$.2f}<extra></extra>',
    showlegend = False))

fig.update_layout(
    hoverlabel_align = 'right',
    title = "Set hover text with hover template")

fig.show(renderer="json")