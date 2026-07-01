import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fs = 10  
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]

fig, ax = plt.subplots(figsize=(5, 4))

ax.violinplot(data, pos, points=80, orientation='horizontal', widths=0.7,
              showmeans=True, showextrema=True, showmedians=True)
ax.set_title('Custom violin 7', fontsize=fs)

ax.set_yticklabels([])

fig.suptitle("Violin Plotting Example 7")
plt.show()