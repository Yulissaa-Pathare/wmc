
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.2)

si = Slider(plt.axes([0.2, 0.1, 0.6, 0.03]), "i", 0, 4, valinit=2, valstep=1)
sj = Slider(plt.axes([0.2, 0.04, 0.6, 0.03]), "j", 0, 4, valinit=1, valstep=1)

def draw(v=None):
    i, j = int(si.val), int(sj.val)
    if i == 0 and j == 0:
        return

    N = i*i + i*j + j*j
    Q = np.sqrt(3*N)
    ax.clear()
    cells = []

    for q in range(-6, 7):
        for r in range(-6, 7):
            x = np.sqrt(3)*(q+r/2)
            y = 1.5*r
            if np.hypot(x, y) > 6:
                continue

            f = (q*(i+j)+r*j) % N
            ax.add_patch(RegularPolygon((x, y), 6, radius=1,
                         facecolor=plt.cm.rainbow(f/N), edgecolor="black"))
            ax.text(x, y, "F"+str(f+1), ha="center", va="center", fontsize=7)
            cells.append((x, y, f))

    x, y, f = next(c for c in cells if c[0] == 0 and c[1] == 0)
    near = min((c for c in cells if c[2] == f and c[:2] != (x, y)),
               key=lambda c: np.hypot(c[0]-x, c[1]-y))

    ax.plot([x, near[0]], [y, near[1]], "k-", linewidth=3)
    ax.set_title(f"N={N}, D/R={Q:.2f}")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.canvas.draw_idle()

si.on_changed(draw)
sj.on_changed(draw)
draw()
plt.show()
