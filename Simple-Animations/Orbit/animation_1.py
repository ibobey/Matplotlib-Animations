import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np
from numpy import pi
from typing import Tuple
import seaborn as sns

sns.set_style('white')
sns.set_context('paper')


def orbit(center: Tuple[float, float], a: float, b: float, angle: float, frames: int = 200):
    theta = np.linspace(0, 2 * np.pi, frames)
    x = center[0] + a * np.cos(theta) * np.cos(angle) - b * np.sin(theta) * np.sin(angle)
    y = center[1] + a * np.cos(theta) * np.sin(angle) + b * np.sin(theta) * np.cos(angle)
    return x, y, frames


frames = 200

orbit_1 = orbit(center=(0,0),
                a=3,
                b=2,
                angle=pi / 4,
                frames=frames)

orbit_2 = orbit(center=(0, 0),
                a=4,
                b=2,
                angle=-pi / 4,
                frames=frames)


fig = plt.figure(figsize=(7, 7))
camera = Camera(fig)


for frame in range(0, frames - 1):

    plt.plot(orbit_1[0],
             orbit_1[1],
             "r-.",
             alpha=0.2)

    plt.plot(orbit_2[0],
             orbit_2[1],
             "g-.",
             alpha=0.2)

    plt.scatter(orbit_1[0][frame],
             orbit_1[1][frame],
             c="r",
             alpha=0.8,
             s=1e2)

    plt.scatter(orbit_2[0][frame],
             orbit_2[1][frame],
             c="g",
             alpha=0.8,
             s=3e2)

    camera.snap()

animation = camera.animate(interval=10,
                           repeat=True)

plt.scatter(0,
            0,
            c="#FFEA00",
            alpha=0.8,
            s=1e4)


plt.grid(True, alpha=0.25, ls="-.")
plt.tight_layout()
plt.show()
