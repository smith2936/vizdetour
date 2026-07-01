import plotly.graph_objects as go

fig = go.Figure(go.Parcats(
    dimensions=[
        {'label': 'Hair',
         'values': ['Black', 'Black', 'Black', 'Brown', 'Brown', 'Brown', 'Red', 'Brown']},
        {'label': 'Eye',
         'values': ['Brown', 'Brown', 'Brown', 'Brown', 'Brown', 'Blue', 'Blue', 'Blue']},
        {'label': 'Sex',
         'values': ['Female', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male']}]
))

fig.show(renderer="json")