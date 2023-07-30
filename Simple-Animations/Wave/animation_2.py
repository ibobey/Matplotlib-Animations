from matplotlib import pyplot as plt
import numpy as np
from numpy import pi,cos,sin,sqrt
from matplotlib.animation import FuncAnimation

"y = amplitude*cos(x/wavelength - time/sqrt(wavelength))"


fig = plt.figure()


axis = plt.axes(xlim=(-12, 12),
                ylim=(-25, 40))


line, = axis.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,


def animate(time):

    x = np.linspace(16*-pi, 16*pi, 2000)

    x_out = x
    y_out = 0

    amp0 = 3
    len0 = 8
    x_out -= amp0 * sin((x / len0) - (time / sqrt(len0)))
    y_out += amp0 * cos((x / len0) - (time / sqrt(len0)))

    amp1 = 0.5
    len1 = 2
    x_out -= amp1 * sin((x / len1) - (time / sqrt(len1)))
    y_out += amp1 * cos((x / len1) - (time / sqrt(len1)))

    amp2 = 2
    len2 = 4
    x_out -= amp2 * sin((x / len2) - (time / sqrt(len2)))
    y_out += amp2 * cos((x / len2) - (time / sqrt(len2)))

    line.set_data(x_out, y_out)
    line2 = plt.fill_between(x_out, y_out, -40 ,color="b", alpha=0.15)

    return line, line2


anim = FuncAnimation(fig, animate,
                     init_func=init,
                     frames=200,
                     interval=50,
                     blit=True,
                     repeat=True)

plt.grid(True, alpha=0.3, ls="-.")
plt.tight_layout()
plt.show()


