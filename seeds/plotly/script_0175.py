import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

hovertext=[]
for i in range(len(df['AAPL.Open'])):
    hovertext.append('Open: '+str(df['AAPL.Open'][i])+'<br>Close: '+str(df['AAPL.Close'][i]))

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'],
                text=hovertext,
                hoverinfo='text'))
fig.show(renderer="json")