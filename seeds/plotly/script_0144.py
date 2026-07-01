import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    values = [40000000, 20000000, 30000000, 10000000],
    labels = ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
    texttemplate = "%{label}: %{value:$,s} <br>(%{percent})",
    textposition = "inside"))

fig.show(renderer="json")