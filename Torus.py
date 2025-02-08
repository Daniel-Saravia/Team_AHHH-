import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection

# Parameters for the torus
R = 5  # Major radius
r = 2  # Minor radius

# Create a grid of u and v values
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u, v)

# Parametric equations for the torus
X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

# Plotting the torus
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
torus = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Torus')
plt.colorbar(torus, shrink=0.5, aspect=5)
plt.show()
