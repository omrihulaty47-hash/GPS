import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 1. Define the bandpass filter function
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    # Design filter using SOS for stability
    sos = signal.butter(order, [lowcut, highcut], btype='bandpass', fs=fs, output='sos')
    # Apply filter with zero phase shift
    return signal.sosfiltfilt(sos, data)

# 2. Example Usage
fs = 5000.0       # Sampling frequency (Hz)
lowcut = 500.0    # Lower cutoff (Hz)
highcut = 1250.0  # Upper cutoff (Hz)
t = np.linspace(0, 0.05, int(0.05 * fs), endpoint=False)
# Create a signal with multiple frequencies
x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t)) + 0.02 * np.cos(2 * np.pi * 600 * t)

# Apply filter
y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)

# 3. Plotting results
plt.plot(t, x, label='Noisy signal')
plt.plot(t, y, label='Filtered signal')
plt.legend(); plt.grid(True); plt.show()