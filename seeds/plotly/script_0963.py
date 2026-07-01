import plotly.graph_objects as go
import pandas as pd

milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']

fig = go.Figure(data=go.Scatter(
    y = time_series,
    mode = 'lines'
))

fig.show(renderer="json")