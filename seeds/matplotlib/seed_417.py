import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

w, h = 256, 256
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)

with cbook.get_sample_data('s1045.ima.gz') as datafile:
    s = datafile.read()
A = np.frombuffer(s, np.uint16).astype(float).reshape((w, h))
extent = (0, 25, 0, 25)

fig, ax = plt.subplot_mosaic([
    ['hopper', 'mri']
], figsize=(7, 3.5))

ax['hopper'].imshow(image)
ax['hopper'].axis('off')  

im = ax['mri'].imshow(A, cmap="hot", origin='upper', extent=extent)

markers = [(15.9, 14.5), (16.8, 15)]
x, y = zip(*markers)
ax['mri'].plot(x, y, 'o')

ax['mri'].set_title('MRI')

plt.show()