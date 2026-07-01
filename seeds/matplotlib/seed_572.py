import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fs = 10  
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]

fig, ax = plt.subplots(figsize=(5, 4))

ax.violinplot(data[-1:], pos[-1:], points=60, widths=0.7,
              showmeans=True, showextrema=True, showmedians=True,
              quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
ax.set_title('Custom violin 5', fontsize=fs)

ax.set_yticklabels([])

fig.suptitle("Violin Plotting Example 5")
plt.show()