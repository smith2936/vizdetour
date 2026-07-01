import plotly.graph_objects as go
from skimage import data
from PIL import Image
import base64
from io import BytesIO

img = data.astronaut()  # numpy array
pil_img = Image.fromarray(img) # PIL image object
prefix = "data:image/png;base64,"
with BytesIO() as stream:
    pil_img.save(stream, format="png")
    base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
fig = go.Figure(go.Image(source=base64_string))
fig.show(renderer="json")