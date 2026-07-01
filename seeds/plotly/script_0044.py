import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[0,0.5,1,1.5,2], y=[0,1,2,1,0],
                    fill='toself', fillcolor='darkviolet',
                    hoveron = 'points+fills', # select where hover is active
                    line_color='darkviolet',
                    text="Points + Fills",
                    hoverinfo = 'text+x+y'))

fig.add_trace(go.Scatter(x=[3,3.5,4,4.5,5], y=[0,1,2,1,0],
                    fill='toself', fillcolor = 'violet',
                    hoveron='points',
                    line_color='violet',
                    text="Points only",
                    hoverinfo='text+x+y'))

fig.update_layout(
    title = "hover on <i>points</i> or <i>fill</i>",
    xaxis_range = [0,5.2],
    yaxis_range = [0,3]
)

fig.show(renderer="json")