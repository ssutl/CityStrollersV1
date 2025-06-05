import math
import numpy as np
import matplotlib.pyplot as plt

# Define physical constants
mu = 4 * math.pi * 1e-7  # Permeability of free space (T·m/A)

# Parameters for the traces (in mm)
trace_spacing = 0.6   # 0.6 mm spacing between traces
trace_count = 16      # Number of traces (you can modify this)

# Create a grid of points where we will compute the magnetic field (in mm)
x_range = np.linspace(-2, trace_spacing * trace_count + 2, 200)  # X range in mm
y_range = np.linspace(-5, 5, 200)  # Y range in mm (-5 mm to 5 mm)
X, Y = np.meshgrid(x_range, y_range)

# Initialize array to store the magnetic field magnitudes
B_field = np.zeros(X.shape)

# Define the Biot-Savart Law (simplified, without current)
def BiotSavart_relative(radius):
    if radius == 0:
        return 0  # Avoid division by zero
    return (mu) / (2 * math.pi * (radius / 1000))  # Convert mm to meters inside the function

# Function to calculate the total magnetic field at each point on the grid from all traces
def total_magnetic_field(X, Y, trace_count, trace_spacing):
    B_total = np.zeros(X.shape)  # Initialize total field
    for i in range(trace_count):
        # Assign x position of each trace, spaced by 0.6 mm
        trace_position_x = i * trace_spacing
        # Loop through all points in the grid
        for row in range(X.shape[0]):
            for col in range(X.shape[1]):
                # Compute the 2D distance from the trace to the grid point using Pythagoras
                radius = np.sqrt((X[row, col] - trace_position_x)**2 + (Y[row, col])**2)
                # Add the contribution of this trace to the total field at this point
                B_total[row, col] += BiotSavart_relative(radius)
    return B_total

# Compute the total magnetic field across the grid for the specified number of traces
B_field = total_magnetic_field(X, Y, trace_count, trace_spacing)


# Plot the magnetic field as a heatmap
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, B_field, cmap='inferno')
plt.colorbar(label='Magnetic Field Strength (Relative)')

# Set custom tick marks for the y-axis
plt.yticks(np.arange(-4, 4.5, 0.5))  # Y-axis ticks from -4 mm to 4 mm, step of 0.5 mm

# Set x-axis labels and grid
plt.title(f'Relative Magnetic Field Distribution for {trace_count} Traces (0.3mm Seperation)')
plt.xlabel('Distance (mm)', fontsize=15)
plt.ylabel('Height (mm)', fontsize=15)
plt.grid(True)
plt.show()
plt.show()