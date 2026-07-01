import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

fig, axd = plt.subplot_mosaic(
    [["image", "density"]],
    layout="constrained",
    width_ratios=[1.05, 2],
)

with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))

axd["image"].imshow(im, cmap="gray")
axd["image"].axis('off')

im_nonzero = im[im.nonzero()]  
axd["density"].hist(im_nonzero, bins=np.arange(0, 2**16+1, 512))
axd["density"].set(xlabel='Intensity (a.u.)', xlim=(0, 2**16),
                   ylabel='MRI density', yticks=[])
axd["density"].minorticks_on()

plt.show()