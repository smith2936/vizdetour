import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=4.5, size=(500,))
x2 = np.random.uniform(low=3, high=6, size=(500,))
y2 = np.random.uniform(low=4.5, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add first scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 0.5'
    )
)

# Add second scatter trace with medium sized markers
# and opacity 1.0
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x2,
        y=y2,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 1.0'
    )
)

# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show(renderer="json")