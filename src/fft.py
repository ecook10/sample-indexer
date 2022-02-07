# chart FFT of an audio sample
import numpy as np
from scipy.io import wavfile
import scipy.fftpack as scp
import matplotlib.pyplot as plt

FILE = 'data\hit.wav'

FREQ_MIN = 20
FREQ_MAX = 20000
FREQ_COUNT = 100
FREQS_X = np.rint(np.power(10, np.linspace(np.log10(FREQ_MIN), np.log10(FREQ_MAX), FREQ_COUNT))).astype(int)

sample_rate, sample_data = wavfile.read(FILE)
fft = np.abs(scp.fft(sample_data))

print(f'sample shape: {sample_data.shape}')
print(f'fft shape: {fft.shape}')

fig, ax = plt.subplots()
ax.plot(FREQS_X, fft[FREQS_X, 0])
plt.show()