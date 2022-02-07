import numpy as np
from scipy.io import wavfile
import scipy.fftpack as scp

# x samples / sec / 1000

MILLIS_PER_CHUNK = 1.0

def printStats(fileName):
    sampleRate, sampleData = wavfile.read(fileName)

    # only analyze full chunks
    samplesPerChunk = sampleRate / 1000 * MILLIS_PER_CHUNK
    fullChunks = sampleData.shape[0] % samplesPerChunk
    chunks = np.reshape(sampleData[:samplesPerChunk*fullChunks], (fullChunks, -1, 2))
    chunkRms = np.sqrt(np.sum(np.power(chunks, 2), axis=1))
    chunkRmsMono = np.mean(chunkRms, axis=1)

    t = np.arange(fullChunks)
    linFit = np.polyfit(t, chunkRmsMono, 1)
    linError = linFit[1][0]
    expFit = np.polyfit(t, chunkRmsMono, 2)
    expError = expFit[1][0]

    fft = np.abs(scp.fft(sampleData))

    durationSecs = sampleData.shape[0] / sampleRate
    fundFreq = np.argmax(fft, axis=1)
    meanFreqLevel = np.mean(fft, axis=1)
    noiseIndex = meanFreqLevel / fft[fundFreq]

    print(f'duration (seconds): {durationSecs}')
    print(f'linear volume decay error: {linError} (coefficients: {linError[0]}')
    print(f'exponential volumn decay error: {expError} (coefficients: {expError[0]}')
    print(f'fundamental frequency (Hz): {fundFreq}')
    print(f'noise level: {noiseIndex}')

printStats('data\hit.wav')