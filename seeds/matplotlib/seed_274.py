import matplotlib.pyplot as plt
import numpy as np


def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample name')


np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]

fig, ax1 = plt.subplots(figsize=(3, 3))

ax1.set_title('Default violin plot')
ax1.set_ylabel('Observed values')
ax1.violinplot(data)

labels = ['A', 'B', 'C', 'D']
set_axis_style(ax1, labels)

plt.subplots_adjust(bottom=0.15)
plt.show()