import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.violinplot(all_data, showmeans=False, showmedians=True)
ax.set_title('Violin plot')
ax.yaxis.grid(True)
ax.set_xticks([y + 1 for y in range(len(all_data))],
              labels=['x1', 'x2', 'x3', 'x4'])
ax.set_xlabel('Four separate samples')
ax.set_ylabel('Observed values')

plt.show()