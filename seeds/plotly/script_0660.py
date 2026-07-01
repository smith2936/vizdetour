import plotly.express as px
from skimage import io
img = io.imread('https://user-images.githubusercontent.com/72614349/179115668-2630e3e4-3a9f-4c88-9494-3412e606450a.jpg')
fig = px.imshow(img)
fig.show(renderer="json")