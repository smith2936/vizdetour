import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fs = 10  
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]

fig, ax = plt.subplots(figsize=(5, 4))

ax.violinplot(data, pos, points=60, widths=0.7, showmeans=True,
              showextrema=True, showmedians=True, bw_method=0.5,
              quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]])
ax.set_title('Custom violin 4', fontsize=fs)

ax.set_yticklabels([])

fig.suptitle("Violin Plotting Example 4")
plt.show()