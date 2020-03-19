# Program that Plots the 
# linear, square and cube
# root of a Function.

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0, 4.0, 80)
y1 = x
y2 = x**2
y3 = x**3
plt.plot(x, y1, 'g.', label="linear")
plt.plot(x, y2, 'r.', label="square")
plt.plot(x, y3, 'b.', label="cube")
plt.legend()
plt.title("Weekly Task 8: Plot of Functions")
plt.savefig("plot.png")
