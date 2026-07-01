import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "2018", orientation = "h", measure = ["relative", "relative", "relative", "relative", "total", "relative",
                                              "relative", "relative", "relative", "total", "relative", "relative", "total", "relative", "total"],
    y = ["Sales", "Consulting", "Maintenance", "Other revenue", "Net revenue", "Purchases", "Material expenses",
       "Personnel expenses", "Other expenses", "Operating profit", "Investment income", "Financial income",
       "Profit before tax", "Income tax (15%)", "Profit after tax"],
    x = [375, 128, 78, 27, None, -327, -12, -78, -12, None, 32, 89, None, -45, None],
    connector = {"mode":"between", "line":{"width":4, "color":"rgb(0, 0, 0)", "dash":"solid"}}
))

fig.update_layout(title = "Profit and loss statement 2018")

fig.show(renderer="json")