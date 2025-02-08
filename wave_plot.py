import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection

# Create a grid of x and y values
x = np.linspace(-20, 20, 70)
y = np.linspace(-20, 20, 70)
X, Y = np.meshgrid(x, y)

# Compute the wave function: z = cos(sqrt(x^2 + y^2))
Z = np.cos(np.sqrt(X**2 + Y**2))

# Create a figure and a 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with a cool colormap
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Set z-axis limits to mimic the LaTeX plot
ax.set_zlim(-5, 5)

# Add a title and color bar for reference
ax.set_title('3D Surface Plot of cos(sqrt(x²+y²))')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()
