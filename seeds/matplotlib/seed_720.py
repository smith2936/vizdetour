import matplotlib.pyplot as plt

def print_text(text):
    fig, ax = plt.subplots(figsize=(6, 1), facecolor="#eefade")
    ax.text(0.5, 0.5, text, ha='center', va='center', size=40)
    ax.axis("off")

plt.rcParams["font.family"] = "sans-serif"
print_text("Hello World! 01")
plt.show()