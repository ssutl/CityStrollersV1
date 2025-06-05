import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os
print(os.getcwd())

# Load the Excel file
df = pd.read_excel('XM3s\Results.xlsx', sheet_name='Impedance Response')
df.columns = df.columns.str.strip()

# Extract frequency and impedance data
freq = df['Frequency (Hz)']
z1 = df['Impedance Z']
z2 = df['Impedance Z.1']
avg_impedance = (z1 + z2) / 2

# Frequency tick labels in Hz/kHz
custom_ticks = [100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 7000,
                9000, 10000, 13000, 15000, 17000, 20000]

def format_khz(x, pos):
    if x >= 1000:
        return f"{int(x / 1000)}k"
    else:
        return f"{int(x)}"

# Plot
plt.figure(figsize=(12, 6))

# Frequency band shading
plt.axvspan(20, 250, color='#99ccff', alpha=0.3, label='Bass')
plt.axvspan(250, 2000, color='#66cc66', alpha=0.3, label='Midrange')
plt.axvspan(2000, 20000, color='#ff9999', alpha=0.3, label='Treble')

# Plot average measurements
plt.plot(freq, avg_impedance, marker='o', label='Average', color='orange')

# Log scale and formatting
plt.xscale('log')
plt.xlim(100, 22000)
plt.xticks(custom_ticks)
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_khz))

# Labels
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (Ohms)')
plt.title('XM3s Impedance vs Frequency (1V BK Precision LCR Meter)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Legend (deduplicated)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# Save and show
plt.tight_layout()
plt.savefig('XM3s\headphone_impedance_plot.png', dpi=300)
plt.show()
