import plotly.express as px
import numpy as np
from skimage import data, filters, img_as_float
img = data.camera()
sigmas = [1, 2, 4]
img_sequence = [filters.gaussian(img, sigma=sigma) for sigma in sigmas]
fig = px.imshow(np.array(img_sequence), facet_col=0, binary_string=True,
                labels={'facet_col':'sigma'})
# Set facet titles
for i, sigma in enumerate(sigmas):
    fig.layout.annotations[i]['text'] = 'sigma = %d' %sigma
fig.show(renderer="json")