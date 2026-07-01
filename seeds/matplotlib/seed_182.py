import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25

fig, ax3 = plt.subplots()
ax3.bar(x, y1, width)
ax3.bar(x + width, y2, width,
        color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])
ax3.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])

plt.show()