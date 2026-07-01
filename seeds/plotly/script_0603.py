import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Box(q1=[ 1, 2, 3 ], median=[ 4, 5, 6 ],
                  q3=[ 7, 8, 9 ], lowerfence=[-1, 0, 1],
                  upperfence=[7, 8, 9], mean=[ 2.2, 2.8, 3.2 ],
                  sd=[ 0.2, 0.4, 0.6 ], notchspan=[ 0.2, 0.4, 0.6 ], name="Precompiled Quartiles"))

fig.show(renderer="json")