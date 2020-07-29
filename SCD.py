import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def equation(x, y):
    return x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-1.0, 1.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([equation(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()