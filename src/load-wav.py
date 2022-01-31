# read WAV file to array + chart
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# FILE = 'data\cajon1.wav'
FILE = 'data\hit.wav'

# read WAV file using scipy.io.wavfile
fs_wav, data_wav = wavfile.read(FILE)

print('Signal Duration = {} seconds'.format(data_wav.shape[0] / fs_wav))

time_wav = np.arange(0, len(data_wav)) / fs_wav
fig, ax = plt.subplots()
ax.plot(time_wav, data_wav[:, 0])
plt.show()