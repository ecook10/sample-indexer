import numpy as np

def get_chunks(data, chunkSize, chunkStride):
    if chunkStride > chunkSize:
        raise ValueError("`chunkStride` cannot be greater than `chunkSize`")

    # e.g. stride = 4, last i = 14 => _4 chunks_ (i = 0, 4, 8, 12)
    lastValidStartIndex = data.size - chunkSize
    numChunks = lastValidStartIndex // chunkStride + 1

    chunks = np.zeros((numChunks, chunkSize))
    for i in range(numChunks):
        start = i * chunkStride
        chunks[i] = data[start:start+chunkSize]

    return chunks

# x = np.arange(100)
# print(get_chunks(x, 15, 1))