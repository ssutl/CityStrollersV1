import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load the Excel file
df = pd.read_excel('Results.xlsx', sheet_name='Impedance Response')
df.columns = df.columns.str.strip()

# Extract data
freq_left = df['Frequency (Hz)']
z1_left = df['Impedance Z']
z2_left = df['Impedance Z.1']
avg_left = (z1_left + z2_left) / 2

freq_right = df['Frequency (Hz).1']
z1_right = df['Impedance Z.2']
z2_right = df['Impedance Z.3']
avg_right = (z1_right + z2_right) / 2

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
plt.axvspan(20, 250, color='#99ccff', alpha=0.3, label='Bass')       # Richer blue
plt.axvspan(250, 2000, color='#66cc66', alpha=0.3, label='Midrange') # Deeper green
plt.axvspan(2000, 20000, color='#ff9999', alpha=0.3, label='Treble') # Warm pink/red


# Impedance curves
plt.plot(freq_left, avg_left, marker='o', label='Left Ear Avg', color='blue')
plt.plot(freq_right, avg_right, marker='s', label='Right Ear Avg', color='orange')

# Log scale + readable format
plt.xscale('log')
plt.xlim(100, 22000)
plt.xticks(custom_ticks)
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_khz))

# Labels
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (Ohms)')
plt.title('Impedance vs Frequency (1V BK Precision LCR Meter)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Clean legend (avoid duplicates from shaded regions)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# Save and show
plt.tight_layout()
plt.savefig('impedance_response_final.png', dpi=300)
plt.show()
