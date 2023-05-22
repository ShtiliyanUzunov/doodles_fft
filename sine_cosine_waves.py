import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal
frequency1 = 5  # Frequency of the sine and cosine waves (in Hz)
frequency2 = 10  # Frequency of the sine and cosine waves (in Hz)
sampling_rate = 100  # Sampling rate (in samples per second)
duration = 2  # Duration of the signal (in seconds)

t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)  # Time vector
signal1 = np.sin(2 * np.pi * frequency1 * t)  # Sampled sine wave
signal2 = np.cos(2 * np.pi * frequency2 * t)  # Sampled cosine wave

# Combine the sine wave and the cosine wave
combined_signal = signal1 + signal2

# Perform the Fast Fourier Transform (FFT)
fft_result = np.fft.fft(combined_signal)
fft_frequency = np.fft.fftfreq(len(combined_signal), 1 / sampling_rate)

# Plot the original combined signal
plt.figure(1)
plt.plot(t, combined_signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original Combined Signal")

# Plot the FFT result (only the positive frequencies)
plt.figure(2)
plt.plot(fft_frequency[:len(fft_frequency)//2], np.abs(fft_result[:len(fft_result)//2]) / len(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Result")

plt.show()