import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1, 2, 3, -1, None, 1, 2, -4, None],
    base = 1000
))

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1.1, 2.2, 3.3, -1.1, None, 1.1, 2.2, -4.4, None],
    base = 1000
))

fig.update_layout(
    waterfallgroupgap = 0.5,
)

fig.show(renderer="json")