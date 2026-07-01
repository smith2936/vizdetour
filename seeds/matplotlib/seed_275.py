import matplotlib.pyplot as plt
import numpy as np


def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample name')


np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]

fig, ax2 = plt.subplots(figsize=(3, 3))

ax2.set_title('Set colors of violins')
ax2.set_ylabel('Observed values')
ax2.violinplot(
    data,
    facecolor=[('yellow', 0.3), ('blue', 0.3), ('red', 0.3), ('green', 0.3)],
    linecolor='black',
)

labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

plt.subplots_adjust(bottom=0.15)
plt.show()