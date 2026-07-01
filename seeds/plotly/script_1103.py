import plotly.express as px
data = [[1, .3, .5, .9],
        [.3, .1, .4, 1],
        [.2, .8, .9, .3]]
fig = px.imshow(data, color_continuous_scale=px.colors.sequential.Cividis_r)
fig.show(renderer="json")