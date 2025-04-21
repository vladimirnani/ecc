import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

init_a = 1
init_b = 1


def f(x, a, b):
    return np.sqrt(x ** 3 - a * x + b)


x = np.linspace(-5, 5, 100_000)

# solution to sqrt has two values negative and positive
y_positive = f(x, init_a, init_b)
y_negative = -f(x, init_a, init_b)

fig, ax = plt.subplots()

line, = ax.plot(x, y_positive)
line_negative, = ax.plot(x, y_negative)

fig.subplots_adjust(bottom=0.50)

ax_slider = fig.add_axes((0.2, 0.25, 0.65, 0.03))
bx_slider = fig.add_axes((0.2, 0.1, 0.65, 0.03))

a_slider = Slider(ax=ax_slider, label='a', valmin=-10, valmax=20, valinit=init_a, )

b_slider = Slider(ax=bx_slider, label='b', valmin=-10, valmax=10, valinit=init_b)


def update(val):
    line.set_ydata(f(x, a_slider.val, b_slider.val))
    line_negative.set_ydata(-f(x, a_slider.val, b_slider.val))

    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()


a_slider.on_changed(update)
b_slider.on_changed(update)

plt.grid(True)
plt.show()
