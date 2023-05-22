
import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal
frequency = 5  # Frequency of the sine wave (in Hz)
sampling_rate = 100  # Sampling rate (in samples per second)
duration = 2  # Duration of the signal (in seconds)

t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)  # Time vector
signal = np.sin(2 * np.pi * frequency * t)  # Sampled sine wave

# Perform the Fast Fourier Transform (FFT)
fft_result = np.fft.fft(signal)
fft_frequency = np.fft.fftfreq(len(signal), 1 / sampling_rate)

# Plot the original signal
plt.figure(1)
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original Signal")

# Plot the FFT result (only the positive frequencies)
plt.figure(2)
plt.plot(fft_frequency[:len(fft_frequency)//2], np.abs(fft_result[:len(fft_result)//2]) / len(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Result")

plt.show()