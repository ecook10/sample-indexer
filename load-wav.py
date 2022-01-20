# Read WAV and MP3 files to array
import os
import numpy as np
from scipy.io import wavfile
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import plotly

# read WAV file using scipy.io.wavfile
fs_wav, data_wav = wavfile.read('data\cajon1.wav')

print('Signal Duration = {} seconds'.
      format(data_wav.shape[0] / fs_wav))