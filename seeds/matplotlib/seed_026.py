import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

heading_font = FontProperties(size='large')

fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    font = FontProperties(weight=weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)

plt.show()