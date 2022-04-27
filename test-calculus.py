from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(-2, 2 , 41)
y = np.linspace(-2, 2 , 41)
X , Y = np.meshgrid(x, y)
Z = X*np.exp(-(X**2 + Y**2))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Z = X*exp(-(X**2 + Y**2))')
#Note: Replace gray by jet for color plot
surf = ax.plot_surface(X, Y, Z, cmap = cm.gray , antialiased=False)
plt.show()

