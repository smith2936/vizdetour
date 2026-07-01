import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

fig, axs = plt.subplots(2, 3)

axs[0, 0].boxplot(data)
axs[0, 0].set_title('basic plot')

axs[0, 1].boxplot(data, notch=True)
axs[0, 1].set_title('notched plot')

axs[0, 2].boxplot(data, sym='gD')
axs[0, 2].set_title('change outlier\npoint symbols')

axs[1, 0].boxplot(data, sym='')
axs[1, 0].set_title("don't show\noutlier points")

axs[1, 1].boxplot(data, sym='rs', orientation='horizontal')
axs[1, 1].set_title('horizontal boxes')

axs[1, 2].boxplot(data, sym='rs', orientation='horizontal', whis=0.75)
axs[1, 2].set_title('change whisker length')

fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                    hspace=0.4, wspace=0.3)

plt.show()