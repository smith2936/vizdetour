import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure()
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7]

heading_font = FontProperties(size='large')

fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
variants = ['normal', 'small-caps']
for k, variant in enumerate(variants):
    font = FontProperties(family='serif', variant=variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)

plt.show()