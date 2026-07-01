import matplotlib.pyplot as plt
from matplotlib import patheffects

fig, ax3 = plt.subplots(figsize=(2.5, 3))
p1, = ax3.plot([0, 1], [0, 1])
leg = ax3.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()