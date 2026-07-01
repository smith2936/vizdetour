import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

plt.show()