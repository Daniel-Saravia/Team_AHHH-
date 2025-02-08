import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection

# Create a grid of u and v values
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 30)
U, V = np.meshgrid(u, v)

# Parametric equations for the Möbius strip
X = (1 + V/2 * np.cos(U/2)) * np.cos(U)
Y = (1 + V/2 * np.cos(U/2)) * np.sin(U)
Z = V/2 * np.sin(U/2)

# Create the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the Möbius strip surface
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')

# Remove tick marks and numbers
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Hide the background panes and grid
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_visible(False)
ax.grid(False)

# Hide the entire axis (removes axis lines, labels, etc.)
ax.set_axis_off()

# Display the plot (just the shape)
plt.show()
