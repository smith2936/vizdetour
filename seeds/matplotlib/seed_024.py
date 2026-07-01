import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6]

heading_font = FontProperties(size='large')

fig.text(0.3, 0.9, 'style', fontproperties=heading_font, **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    font = FontProperties(family='sans-serif', style=style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)

plt.show()