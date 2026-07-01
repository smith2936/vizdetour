import plotly.express as px
from skimage import data
img = data.camera()
for compression_level in range(0, 9):
    fig = px.imshow(img, binary_string=True, binary_compression_level=compression_level)
    print(f"compression level {compression_level}: length of {len(fig.data[0].source)}")
fig.show(renderer="json")