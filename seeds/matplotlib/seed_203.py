import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(range(11), color="0.9")

ax.set_title(r"$Title\ in\ math\ mode:\ \int_{0}^{\infty } x^2 dx$",
             math_fontfamily='stixsans', size=14)

plt.show()