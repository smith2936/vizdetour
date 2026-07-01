import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      customdata = ["Long name A1", "Long name A2", "Long name B1", "Long name B2",
                    "Long name C1", "Long name C2"],
      hovertemplate='Node %{customdata} has total value %{value}<extra></extra>',
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2],
      customdata = ["q","r","s","t","u","v"],
      hovertemplate='Link from node %{source.customdata}<br />'+
        'to node%{target.customdata}<br />has value %{value}'+
        '<br />and data %{customdata}<extra></extra>',
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show(renderer="json")