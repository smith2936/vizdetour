import plotly.graph_objects as go
import pandas as pd

dfd = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')
textd = ['non-diabetic' if cl==0 else 'diabetic' for cl in dfd['Outcome']]

fig = go.Figure(data=go.Splom(
                  dimensions=[dict(label='Pregnancies', values=dfd['Pregnancies']),
                              dict(label='Glucose', values=dfd['Glucose']),
                              dict(label='BloodPressure', values=dfd['BloodPressure']),
                              dict(label='SkinThickness', values=dfd['SkinThickness']),
                              dict(label='Insulin', values=dfd['Insulin']),
                              dict(label='BMI', values=dfd['BMI']),
                              dict(label='DiabPedigreeFun', values=dfd['DiabetesPedigreeFunction']),
                              dict(label='Age', values=dfd['Age'])],
                  marker=dict(color=dfd['Outcome'],
                              size=5,
                              colorscale='Bluered',
                              line=dict(width=0.5,
                                        color='rgb(230,230,230)')),
                  text=textd,
                  diagonal=dict(visible=False)))

title = "Scatterplot Matrix (SPLOM) for Diabetes Dataset<br>Data source:"+\
        " <a href='https://www.kaggle.com/uciml/pima-indians-diabetes-database/data'>[1]</a>"
fig.update_layout(title=title,
                  dragmode='select',
                  width=1000,
                  height=1000,
                  hovermode='closest')

fig.show(renderer="json")