import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-5.0, 5.0, 0.1)
# y = 2*x**2-5

# plt.plot(x, y)
# plt.show()


x = np.arange(0,361,1)
y = np.sin(np.radians(x))

plt.plot(x, y)
plt.show()


