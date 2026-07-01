import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Cone(x=[1,] * 3, name="base"))
fig.add_trace(go.Cone(x=[2,] * 3, opacity=0.3, name="opacity:0.3"))
fig.add_trace(go.Cone(x=[3,] * 3, lighting_ambient=0.3, name="lighting.ambient:0.3"))
fig.add_trace(go.Cone(x=[4,] * 3, lighting_diffuse=0.3, name="lighting.diffuse:0.3"))
fig.add_trace(go.Cone(x=[5,] * 3, lighting_specular=2, name="lighting.specular:2"))
fig.add_trace(go.Cone(x=[6,] * 3, lighting_roughness=1, name="lighting.roughness:1"))
fig.add_trace(go.Cone(x=[7,] * 3, lighting_fresnel=2, name="lighting.fresnel:2"))
fig.add_trace(go.Cone(x=[8,] * 3, lightposition=dict(x=0, y=0, z=1e5),
                                  name="lighting.position x:0,y:0,z:1e5"))

fig.update_traces(y=[1, 2, 3], z=[1, 1, 1],
                  u=[1, 2, 3], v=[1, 1, 2], w=[4, 4, 1],
                  hoverinfo="u+v+w+name",
                  showscale=False)

fig.update_layout(scene=dict(aspectmode="data",
                             camera_eye=dict(x=0.05, y=-2.6, z=2)),
                  margin=dict(t=0, b=0, l=0, r=0))


fig.show(renderer="json")