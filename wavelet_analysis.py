import pywt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from both CSV files
data1 = pd.read_csv('P006_S002.csv')
data2 = pd.read_csv('P006_S001.csv')

# Extract 'Road Position (m)' data
road_position1 = data1['Road Position (m)']
road_position2 = data2['Road Position (m)']

# Convert time to minutes
time_values1 = data1['Time'] / 60
time_values2 = data2['Time'] / 60

# Create figure for subplots
plt.figure(figsize=[15, 18])

# Plot Road Position from both experiments
ax1 = plt.subplot(3, 1, 1)
ax1.plot(time_values1, road_position1, 'blue', alpha=0.5, label='Exp S002')
ax1.plot(time_values2, road_position2, 'red', alpha=0.5, label='Exp S001')
ax1.set_title('Road Position (m) over Time')
ax1.set_xlabel('Time (minutes)')
ax1.set_ylabel('Road Position (m)')
ax1.grid(True)
ax1.legend()

# Plot Steering Position from both experiments
ax2 = plt.subplot(3, 1, 2)
ax2.plot(time_values1, data1['Steering Position'], 'green', alpha=0.5, label='Exp S002')
ax2.plot(time_values2, data2['Steering Position'], 'purple', alpha=0.5, label='Exp S001')
ax2.set_title('Steering Position over Time')
ax2.set_xlabel('Time (minutes)')
ax2.set_ylabel('Steering Position')
ax2.grid(True)
ax2.legend()

# Plot Speed from both experiments
ax3 = plt.subplot(3, 1, 3)
ax3.plot(time_values1, data1['Speed (kph)'], 'orange', alpha=0.5, label='Exp S002')
ax3.plot(time_values2, data2['Speed (kph)'], 'black', alpha=0.5, label='Exp S001')
ax3.set_title('Speed (kph) over Time')
ax3.set_xlabel('Time (minutes)')
ax3.set_ylabel('Speed (kph)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.show()
wavelet_road_position=road_position1
# Downsampling the signal to 1 Hz for the wavelet analysis
original_sampling_rate = 25  # Hz
new_sampling_rate = 8 # Hz
downsample_factor = int(original_sampling_rate / new_sampling_rate)  # original sampling rate is 25 Hz
downsampled_road_position1 = wavelet_road_position[::downsample_factor]
downsampled_time_values1 = np.linspace(time_values1.iloc[0], time_values1.iloc[-1], num=len(downsampled_road_position1))

time_start_1=5
time_stop_1=90
# Selecting the specific time segment between 15 and 25 minutes for the downsampled data
start_index = int(time_start_1 * new_sampling_rate)  # Convert 15 minutes to samples in the downsampled data
end_index = int(time_stop_1 * new_sampling_rate)  # Convert 25 minutes to samples in the downsampled data

specific_road_position = downsampled_road_position1[start_index:end_index]
# Adjustments for the correct specific time range after downsampling
# Assuming we've already downsampled the data correctly as in the previous steps
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Define the frequency range
import pywt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Your existing data loading and plotting code...

# After downsampling and slicing the section of interest...

# New frequency range
min_freq = 0.01  # Minimum frequency in Hz
max_freq = 0.015  # Maximum frequency in Hz

# Convert these frequencies to scales for Morlet wavelet
center_frequency_of_wavelet = 6  # Typical value for Morlet wavelet
min_scale = new_sampling_rate / (max_freq * center_frequency_of_wavelet)
max_scale = new_sampling_rate / (min_freq * center_frequency_of_wavelet)

# Create an array of scales
scales = np.arange(np.floor(max_scale), np.ceil(min_scale), -1)  # High scales (low freq) to low scales (high freq)

# Perform the continuous wavelet transform using these scales
coefficients, frequencies = pywt.cwt(specific_road_position, scales, 'morl', sampling_period=1/new_sampling_rate)

# Plotting the focused CWT results
plt.figure(figsize=[15, 6])
# Note: Adjust the extent if your plot's time does not match your data slice.
# Since you're interested in the segment from 15 to 25 minutes after downsampling, ensure this matches your data slice.
plt.imshow(abs(coefficients), extent=[time_start_1, time_stop_1, min_freq, max_freq], aspect='auto', cmap='jet',
           vmax=abs(coefficients).max(), vmin=abs(coefficients).min())
plt.yscale('log')  # Log scale for frequencies
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (minutes)')
plt.colorbar(label='Magnitude')
plt.title('Continuous Wavelet Transform (CWT) Focused on 0.001 Hz to 0.01 Hz')
plt.show()
