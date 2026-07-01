import plotly.graph_objects as go

annotation_template = go.layout.Template()
annotation_template.layout.annotationdefaults = dict(font=dict(color="crimson"))

fig = go.Figure()
fig.update_layout(
     template=annotation_template,
     annotations=[
         dict(text="Look Here", x=1, y=1),
         dict(text="Look There", x=2, y=2)
     ]
 )
fig.show(renderer="json")