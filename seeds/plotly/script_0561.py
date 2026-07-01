import plotly.figure_factory as ff
import numpy as np
np.random.seed(1)

z = np.random.randn(20, 20)
z_text = np.around(z, decimals=2) # Only show rounded value (full value on hover)

fig = ff.create_annotated_heatmap(z, annotation_text=z_text, colorscale='Greys',
                                  hoverinfo='z')

# Make text size smaller
for i in range(len(fig.layout.annotations)):
    fig.layout.annotations[i].font.size = 8

fig.show(renderer="json")