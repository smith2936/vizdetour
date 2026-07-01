import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

n_samples, n_rows = 800, 4
with cbook.get_sample_data('eeg.dat') as eegfile:
    data = np.fromfile(eegfile, dtype=float).reshape((n_samples, n_rows))
t = 10 * np.arange(n_samples) / n_samples

fig, ax = plt.subplots(layout="constrained")
ax.set_xlabel('Time (s)')
ax.set_xlim(0, 10)
dy = (data.min() - data.max()) * 0.7  
ax.set_ylim(-dy, n_rows * dy)
ax.set_yticks([0, dy, 2*dy, 3*dy], labels=['PG3', 'PG5', 'PG7', 'PG9'])

for i, data_col in enumerate(data.T):
    ax.plot(t, data_col + i*dy, color="C0")

plt.show()