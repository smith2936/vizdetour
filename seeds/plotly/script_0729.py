import plotly.graph_objects as go

fig = go.Figure(go.Parcats(
    dimensions=[
        {'label': 'Hair',
         'values': ['Black', 'Brown', 'Brown', 'Brown', 'Red']},
        {'label': 'Eye',
         'values': ['Brown', 'Brown', 'Brown', 'Blue', 'Blue']},
        {'label': 'Sex',
         'values': ['Female', 'Male', 'Female', 'Male', 'Male']}],
    counts=[6, 10, 40, 23, 7]
))


fig.show(renderer="json")