import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

heading_font = FontProperties(size='large')

fig.text(0.9, 0.9, 'size', fontproperties=heading_font, **alignment)
sizes = ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    font = FontProperties(size=size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)

plt.show()