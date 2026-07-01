import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x='petal_width', y='sepal_length', color='species')

fig.update_layout(
    dragmode='drawopenpath',
    newshape_line_color='cyan',
    title_text='Draw a path to separate versicolor and virginica',
    modebar_add=['drawline',
        'drawopenpath',
        'drawclosedpath',
        'drawcircle',
        'drawrect',
        'eraseshape'
       ]
)

fig.show(renderer="json")