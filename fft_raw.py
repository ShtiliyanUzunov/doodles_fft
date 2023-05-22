import numpy as np


def cooley_tukey_fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = cooley_tukey_fft(x[0::2])
    odd = cooley_tukey_fft(x[1::2])

    T = np.exp(-2j * np.pi * np.arange(N // 2) / N) * odd

    return np.concatenate([even + T, even - T])


# Example usage:
signal = np.array([1, 0, -1, 0])
fft_result = cooley_tukey_fft(signal)
print(fft_result)