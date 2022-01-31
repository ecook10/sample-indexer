# Read WAV and MP3 files to array
import os
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# FILE = 'data\cajon1.wav'
FILE = 'data\hit.wav'

# read WAV file using scipy.io.wavfile
fs_wav, data_wav = wavfile.read(FILE)

print('Signal Duration = {} seconds'.format(data_wav.shape[0] / fs_wav))

time_wav = np.arange(0, len(data_wav)) / fs_wav
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(time_wav, data_wav[:, 0]);  # Plot some data on the axes.
plt.show()