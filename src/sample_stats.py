import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from chunky import get_chunks

class SampleAmp:

    def __init__(self, sampleDataMono, chunkSize, chunkStride):
        self.chunks = get_chunks(sampleDataMono, chunkSize, chunkStride or chunkSize).astype('int64')
        self.chunkRms = np.sqrt(np.sum(np.power(self.chunks, 2), axis=1))

        t = np.arange(self.chunks.shape[0])
        self.linFit = np.polyfit(t, self.chunkRms, 1, full=True)
        self.expFit = np.polyfit(t, self.chunkRms, 2, full=True)
        self.linError = self.linFit[1][0]
        self.expError = self.expFit[1][0]


class SampleFreqs:

    def __init__(self, sampleRate, sampleDataMono):
        N = sampleDataMono.shape[0]
        self.fftValues = (np.abs(fft(sampleDataMono)) * (2 / N))[0:N//2]
        self.fftFreqs = fftfreq(sampleDataMono.shape[0], 1 / sampleRate)[0:N//2]

        iFundFreq = np.argmax(self.fftValues)
        self.fundFreqs = self.fftFreqs[iFundFreq]
        self.noiseIndex = np.mean(self.fftValues / self.fftValues[iFundFreq])


class SampleStats:

    def __init__(self, fileName, chunkSize=100, chunkStride=10):
        sampleRate, sampleData = wavfile.read(fileName)

        self.sampleRate = sampleRate
        self.sampleData = sampleData
        self.sampleDataMono = sampleData[:,0] if (sampleData.ndim == 2) else sampleData
        self.durationSecs = sampleData.shape[0] / sampleRate
        self.amp = SampleAmp(self.sampleDataMono, chunkSize, chunkStride)
        self.freqs = SampleFreqs(sampleRate, self.sampleDataMono)

    def __str__(self):
        return f"""
        duration (seconds): {self.durationSecs}
        linear volume decay error: {self.amp.linError} (coefficients: {self.amp.linFit[0]}
        exponential volumn decay error: {self.amp.expError} (coefficients: {self.amp.expFit[0]}
        fundamental frequency (Hz): {self.freqs.fundFreqs}
        noise level: {self.freqs.noiseIndex}
        """

# stats = SampleStats('data\snap.wav')
# print(str(stats))