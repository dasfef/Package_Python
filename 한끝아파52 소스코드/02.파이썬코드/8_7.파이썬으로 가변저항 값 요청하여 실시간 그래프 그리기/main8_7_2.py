from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

max_x_points = 200

fig = plt.figure()
ax = plt.axes(xlim=(0, max_x_points), ylim=(0, 1023))

line, = ax.plot(np.arange(max_x_points), 
                np.ones(max_x_points, dtype=np.float)*np.nan, lw=2)

def init():
    return line,

def animate(i):
    y = random.randint(0,1023)
    print(y)
    y = float(y)

    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)

plt.show()