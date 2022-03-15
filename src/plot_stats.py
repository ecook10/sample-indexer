import numpy as np
import matplotlib.pyplot as plt
from sample_stats import SampleStats
from chunky import get_chunks

def plot_signal(stats):
    plt.plot(np.arange(stats.sampleData.shape[0]), stats.sampleData)
    plt.show()

def plot_rms(amp):
    print(amp.chunkRms)
    plt.plot(np.arange(amp.chunkRms.shape[0]), amp.chunkRms)
    plt.show()

def plot_fft(freqs):
    plt.plot(freqs.fftFreqs, freqs.fftValues)
    plt.show()

stats = SampleStats('data\snap.wav', 2000)

# plot_signal(stats)
# plot_fft(stats.freqs)
plot_rms(stats.amp)

print(stats.sampleDataMono.shape)
print(stats.amp.chunks.shape)