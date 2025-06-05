import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load Excel data
df = pd.read_excel('XM3s/Results.xlsx', sheet_name='Voltage Response at High-z')
df.columns = df.columns.str.strip()

# Extract data from both measurements (not left/right)
freq = df['Frequency (Hz)']
voltage = df['Voltage Across Load (mVAC)']

# Custom ticks
custom_ticks = [20, 31.5, 50, 80, 100, 200, 500, 1000, 2000, 5000, 10000, 15000, 20000]

def format_khz(x, pos):
    if x == 31.5:
        return "31.5"
    return f"{int(x / 1000)}k" if x >= 1000 else f"{int(x)}"

# Plot both measurements
plt.figure(figsize=(12, 6))

# Frequency bands
plt.axvspan(20, 250, color='#99ccff', alpha=0.3, label='Bass')
plt.axvspan(250, 2000, color='#66cc66', alpha=0.3, label='Midrange')
plt.axvspan(2000, 20000, color='#ff9999', alpha=0.3, label='Treble')

# Voltage plots
plt.plot(freq, voltage, marker='o', color='orange', label='Measurement 2')

# Axes
plt.xscale('log')
plt.xlim(20, 22000)
plt.xticks(custom_ticks)
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_khz))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.2f}"))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage Across Load (mVAC)')
plt.title('XM3s Voltage vs Frequency (High-Z Load, 1Vpp Input)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# Save + show
plt.tight_layout()
plt.savefig('XM3s/voltage_response_combined.png', dpi=300)
plt.show()
