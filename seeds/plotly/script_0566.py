import plotly.graph_objects as go

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planet_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
                 'rgb(178, 0, 0)', 'rgb(235, 235, 210)', 'rgb(235, 205, 130)',
                 'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(255, 255, 255)']
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# Create trace, sizing bubbles by planet diameter
fig = go.Figure(data=go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plotly.com/python/reference/scatter/#scatter-marker-sizeref
        size = planet_diameter,
        color = planet_colors,
        )
))

fig.update_layout(
    width=800,
    height=800,
    title=dict(text="Planets!"),
    scene=dict(
        xaxis=dict(
            title=dict(
                text="Distance from Sun",
                font=dict(
                    color="white"
                )
            )
        ),
        yaxis=dict(
            title=dict(
                text="Density",
                font=dict(
                    color="white"
                )
            )
        ),
        zaxis=dict(
            title=dict(
                text="Gravity",
                font=dict(
                    color="white"
                )
            )
        ),
        bgcolor="rgb(20, 24, 54)"
    )
)

fig.show(renderer="json")