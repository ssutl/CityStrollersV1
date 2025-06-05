import numpy as np
import matplotlib.pyplot as plt

# Parameters
w_b = 12e-3  # Bundle width
w_t = 0.3e-3  # Track width
w_c = 0.3e-3  # Clearance

# Number of turns (Dependent)
NoT = int(w_b / (w_t + w_c))

# Number of folds
NoF = 2

# Height of stroke
h = 50e-3

# Number of points for circle
NoPC = 32

# Initialize buffer
NoP = 10000
X = np.zeros(NoP)
Y = np.zeros(NoP)

X[0] = 0
Y[0] = 0
pointer = 0

# Starting point is left bottom corner of the outmost turn
for i in range(1, NoT + 1):
    for j in range(1, NoF + 1):
        # Add a straight segment up
        pointer += 1
        X[pointer] = X[pointer - 1]
        Y[pointer] = Y[pointer - 1] + h

        # Add a 1/2 circle to the right
        radius = (NoT + 0.5 - i) * (w_t + w_c)
        x_centre = X[pointer] + radius
        y_centre = Y[pointer]

        for k in range(1, NoPC // 2 + 1):
            theta = np.pi - k * (2 * np.pi / NoPC)
            pointer += 1
            X[pointer] = x_centre + np.cos(theta) * radius
            Y[pointer] = y_centre + np.sin(theta) * radius

        # Add a straight segment down
        pointer += 1
        X[pointer] = X[pointer - 1]
        Y[pointer] = Y[pointer - 1] - h

        if j != NoF:
            # Add a 1/2 circle to the down and right
            radius = (i - 0.5) * (w_t + w_c)
            x_centre = X[pointer] + radius
            y_centre = Y[pointer]

            for k in range(1, NoPC // 2 + 1):
                theta = np.pi + k * (2 * np.pi / NoPC)
                pointer += 1
                X[pointer] = x_centre + np.cos(theta) * radius
                Y[pointer] = y_centre + np.sin(theta) * radius
        else:
            # Add a 1/4 circuit to the down and left
            radius = w_b + (NoT + 0.5 - i) * (w_t + w_c)
            x_centre = X[pointer] - radius
            y_centre = Y[pointer]

            for k in range(1, NoPC // 4 + 1):
                theta = 0 - k * (2 * np.pi / NoPC)
                pointer += 1
                X[pointer] = x_centre + np.cos(theta) * radius
                Y[pointer] = y_centre + np.sin(theta) * radius

            # Add a segment to the left
            pointer += 1
            X[pointer] = X[pointer - 1] - (2 * (NoF - 2) * w_b) + (w_t + w_c)
            Y[pointer] = Y[pointer - 1]

            # Add a 1/4 circuit to the up and left
            radius = w_b + (NoT + 0.5 - i) * (w_t + w_c)
            x_centre = X[pointer]
            y_centre = Y[pointer] + radius

            for k in range(1, NoPC // 4 + 1):
                theta = (-np.pi / 2) - k * (2 * np.pi / NoPC)
                pointer += 1
                X[pointer] = x_centre + np.cos(theta) * radius
                Y[pointer] = y_centre + np.sin(theta) * radius

# Trim unused points
X = X[:pointer + 1]
Y = Y[:pointer + 1]

# Function to calculate trace resistance
def calculate_trace_resistance(X, Y, resistivity=1.68e-8, trace_thickness=35e-6):
    """
    Calculate the resistance of the entire trace.
    
    Parameters:
    - X, Y: Arrays of x and y coordinates of the trace.
    - resistivity: Electrical resistivity of the material (Ω·m), default is for copper.
    - trace_thickness: Thickness of the trace (m), default is 35 µm (typical PCB copper thickness).

    Returns:
    - Total resistance of the trace (Ω).
    """
    total_length = np.sum(np.sqrt(np.diff(X)**2 + np.diff(Y)**2))
    cross_sectional_area = w_t * trace_thickness
    resistance = resistivity * total_length / cross_sectional_area
    return resistance

# Compute trace resistance
trace_resistance = calculate_trace_resistance(X, Y)
print(f"Total trace resistance: {trace_resistance:.6f} Ohms")


# Plot the results
plt.figure()
plt.plot(X, Y)
plt.axis('equal')
plt.title("Single Layer Track Plot")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
plt.show()
