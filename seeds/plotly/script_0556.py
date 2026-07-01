import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
       ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [10, 20, 30, -10, None, 10, 20, -40, None], base = 300,
    decreasing = {"marker":{"color":"Maroon", "line":{"color":"red", "width":2}}},
    increasing = {"marker":{"color":"Teal"}},
    totals = {"marker":{"color":"deep sky blue", "line":{"color":"blue", "width":3}}}
))

fig.update_layout(title = "Profit and loss statement", waterfallgap = 0.3)

fig.show(renderer="json")