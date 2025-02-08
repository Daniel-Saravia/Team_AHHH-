import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute z = x^2 - y^2
Z = X**2 - Y**2

# Plotting the hyperbolic paraboloid
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
saddle = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
ax.set_title('Hyperbolic Paraboloid (Saddle Surface)')
plt.colorbar(saddle, shrink=0.5, aspect=5)
plt.show()
