import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# The Iris dataset contains four data variables, sepal length, sepal width, petal length,
# petal width, for 150 iris flowers. The flowers are labeled as `Iris-setosa`,
# `Iris-versicolor`, `Iris-virginica`.

# Define indices corresponding to flower categories, using pandas label encoding
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width']),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                text=df['class'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))


fig.update_layout(
    title=dict(text='Iris Data set'),
    dragmode='select',
    width=600,
    height=600,
    hovermode='closest',
)

fig.show(renderer="json")