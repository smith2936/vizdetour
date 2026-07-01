import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter

prng = np.random.RandomState(19680801)
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2

fig, ax0 = plt.subplots(figsize=(7, 4.8))
ax0.set_xscale('log')
ax0.set_title('Full unit ticklabels, w/ default precision & space separator')
formatter0 = EngFormatter(unit='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')
plt.tight_layout()
plt.show()