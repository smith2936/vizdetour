import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]],
                    text=[['one', 'twenty', 'thirty'],
                          ['twenty', 'one', 'sixty'],
                          ['thirty', 'sixty', 'one']],
                    texttemplate="%{text}",
                    textfont={"size":20}))

fig.show(renderer="json")