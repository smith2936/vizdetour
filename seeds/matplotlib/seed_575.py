import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fs = 10  
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]

fig, ax = plt.subplots(figsize=(5, 4))

ax.violinplot(data, pos, points=100, orientation='horizontal', widths=0.9,
              showmeans=True, showextrema=True, showmedians=True,
              bw_method='silverman')
ax.set_title('Custom violin 8', fontsize=fs)

ax.set_yticklabels([])

fig.suptitle("Violin Plotting Example 8")
plt.show()