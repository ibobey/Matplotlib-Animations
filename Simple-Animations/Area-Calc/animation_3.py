from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import sympy as sp
from scipy.integrate import trapz

a = sp.symbols("a")
expr = (a+1) * (a-2) * (a+2) * (a-1) + 1
f = sp.lambdify(a, expr)


fig = plt.figure(figsize=(9,6))

axis = plt.axes(xlim=(-3, 3),
                ylim=(-3, 15))

line, = axis.plot([], [], "k")
line2, = axis.plot([], [], lw=3)


x_vals, y_vals = [], []


x = np.linspace(-2.1,2.1,500)

def animate(time):
    fig.clear()

    plt.xlim(-2.2,2.3)
    plt.ylim(-2,5.3)
    x_vals.append(time)
    y_vals.append(f(time))

    plt.plot(x_vals, y_vals,"k-")
    plt.fill_between(x_vals,
                     y_vals,
                     0,
                     color="b",
                     alpha=0.15)

    plt.grid(True, alpha=0.3, ls="-.")

    integral = trapz(y_vals,x_vals)
    plt.figtext(0.05, 0.01, f"Integral: {round(integral,3)}", fontsize=16, va="bottom", ha="left")
    plt.axhline(0,color="r",alpha=0.15)


anim = FuncAnimation(fig,
                     animate,
                     frames=x,
                     interval=20,
                     repeat=False)

plt.show()
