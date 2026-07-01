import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 
nse2 = np.random.randn(len(t))                 

s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, ax = plt.subplots(layout='constrained')
cxy, f = ax.cohere(s1, s2, NFFT=256, Fs=1. / dt)
ax.set_ylabel('Coherence')

plt.show()