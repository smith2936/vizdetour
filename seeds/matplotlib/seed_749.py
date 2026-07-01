import matplotlib.pyplot as plt
import numpy as np

fig, ax0 = plt.subplots(figsize=(3.5, 4))

ax0.set_aspect(1)
ax0.plot(np.arange(10))
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')

ax0.grid()

plt.show()