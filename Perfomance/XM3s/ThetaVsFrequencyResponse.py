import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load the Excel file
df = pd.read_excel('XM3s/Results.xlsx', sheet_name='Impedance Response')
df.columns = df.columns.str.strip()

# Extract data
freq1 = df['Frequency (Hz)']
theta1 = df['Theta']
theta2 = df['Theta.1']
avg_theta = (theta1 + theta2) / 2

# Frequency ticks
custom_ticks = [100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 7000,
                9000, 10000, 13000, 15000, 17000, 20000]

def format_khz(x, pos):
    return f"{int(x / 1000)}k" if x >= 1000 else f"{int(x)}"

# Plot
plt.figure(figsize=(12, 6))

# Shading frequency bands
plt.axvspan(20, 250, color='#99ccff', alpha=0.3, label='Bass')
plt.axvspan(250, 2000, color='#66cc66', alpha=0.3, label='Midrange')
plt.axvspan(2000, 20000, color='#ff9999', alpha=0.3, label='Treble')

# Theta plots
plt.plot(freq1, avg_theta, marker='o', label='Average Theta', color='orange')

# Axis scale and formatting
plt.xscale('log')
plt.xlim(100, 22000)
plt.xticks(custom_ticks)
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_khz))

# Labels
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase Angle (Theta, degrees)')
plt.title('XM3s Phase Angle vs Frequency (1V BK Precision LCR Meter)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Clean legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# Save and show
plt.tight_layout()
plt.savefig('XM3s/theta_response_final.png', dpi=300)
plt.show()
