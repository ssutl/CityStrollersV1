import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load Excel data
df = pd.read_excel('Results.xlsx', sheet_name='Voltage Response at High-z')
df.columns = df.columns.str.strip()

# Extract data
freq_left = df['Frequency (Hz)']
voltage_left = df['Voltage Across Load (mVAC)']
freq_right = df['Frequency (Hz).1']
voltage_right = df['Voltage Across Load (mVAC).1']

# Custom ticks
custom_ticks = [20, 31.5, 50, 80, 100, 200, 500, 1000, 2000, 5000, 10000, 15000, 20000]

def format_khz(x, pos):
    if x >= 1000:
        return f"{int(x / 1000)}k"
    elif x == 31.5:
        return "31.5"
    else:
        return f"{int(x)}"

# Plot both Left and Right on same graph
plt.figure(figsize=(12, 6))

# Frequency bands
plt.axvspan(20, 250, color='#99ccff', alpha=0.3, label='Bass')
plt.axvspan(250, 2000, color='#66cc66', alpha=0.3, label='Midrange')
plt.axvspan(2000, 20000, color='#ff9999', alpha=0.3, label='Treble')

# Voltage plots
plt.plot(freq_left, voltage_left, marker='o', color='blue', label='Left Ear Avg')
plt.plot(freq_right, voltage_right, marker='s', color='orange', label='Right Ear Avg')

# Axes
plt.xscale('log')
plt.xlim(20, 22000)
plt.xticks(custom_ticks)
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_khz))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.2f}"))  # <- formats y ticks
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage Across Load (mVAC)')
plt.title('Voltage vs Frequency (High-Z Load, 1Vpp Input)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.tight_layout()
plt.savefig('voltage_response_combined.png', dpi=300)
plt.show()
