import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

# x samples / sec / 1000

MILLIS_PER_CHUNK = 1

class SampleStats:

    def __init__(self, fileName):
        sampleRate, sampleData = wavfile.read(fileName)

        # only analyze full chunks
        samplesPerChunk = sampleRate // 1000 * MILLIS_PER_CHUNK
        fullChunks = sampleData.shape[0] % samplesPerChunk
        chunks = np.reshape(sampleData[:samplesPerChunk*fullChunks], (fullChunks, -1, 2))
        chunkRms = np.sqrt(np.sum(np.power(chunks, 2), axis=1))
        chunkRmsMono = np.mean(chunkRms, axis=1)

        t = np.arange(fullChunks)
        linFit = np.polyfit(t, chunkRmsMono, 1, full=True)
        expFit = np.polyfit(t, chunkRmsMono, 2, full=True)

        fftValues = np.abs(fft(sampleData))
        fftFreqs = fftfreq(sampleData.shape[0], 1 / sampleRate)

        fundFreqIndices = np.argmax(fftValues, axis=0)
        fundFreqs = fftFreqs[fundFreqIndices]

        meanFftValues = np.mean(fftValues, axis=0)
        noiseIndex = np.mean(np.array([meanFftValues[i] / fftValues[fundFreqIndices[i], i] for i in range(fundFreqIndices.size)]))

        self.durationSecs = sampleData.shape[0] / sampleRate
        self.linFit = linFit
        self.expFit = expFit
        self.fundFreqs = fundFreqs
        self.noiseIndex = noiseIndex

    def linError(self):
        self.linFit[1][0]

    def expError(self):
        self.expFit[1][0]

    def __str__(self):
        return f"""
        duration (seconds): {self.durationSecs}
        linear volume decay error: {self.linError()} (coefficients: {self.linFit[0]}
        exponential volumn decay error: {self.expError()} (coefficients: {self.expFit[0]}
        fundamental frequency (Hz): {self.fundFreqs}
        noise level: {self.noiseIndex}
        """

stats = SampleStats('data\piano-chord.wav')
print(str(stats))