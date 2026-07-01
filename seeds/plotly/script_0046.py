import plotly.graph_objects as go

fig = go.Figure(
    data=[
      go.Bar(
        x=["A", "B", "C", "D"],
        y=[10, 15, 13, 17]
        )
    ],
    layout=dict(
      title=dict(
        text="Chart Title",
        font=dict(
          size=40
          )
        )
      ),
    # Previously the title font could be set like this:
    # titlefont=dict(size=40)
)

fig.show(renderer="json")