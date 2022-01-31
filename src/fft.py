# chart FFT of an audio sample
import numpy as np
from scipy.io import wavfile
import scipy.fftpack as scp
import matplotlib.pyplot as plt

FILE = 'data\hit.wav'

sample_rate, sample_data = wavfile.read(FILE)
fft = np.abs(scp.fft(sample_data))

print(f'sample shape: {sample_data.shape}')
print(f'fft shape: {fft.shape}')

time_wav = np.arange(0, len(sample_data)) / sample_rate
fig, ax = plt.subplots()
ax.plot(fft[:, 0])
plt.show()