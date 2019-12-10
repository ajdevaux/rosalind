import numpy as np

seq = 'CATACATTTAAGCACTCAGTAAGCTTAGCGGGGCGGAGTTCCGGGGCGCAGGTGGAGCCAGAGATTGGCATAGATAGCAATCCCC'

GC_arr = [0.077, 0.127, 0.198, 0.259, 0.312, 0.344, 0.410, 0.447, 0.503, 0.590, 0.618, 0.694, 0.738, 0.828, 0.841, 0.893]

prob_arr = []
for val in GC_arr:
    GC_content = val
    GC_freq = GC_content / 2
    AT_freq = (1-GC_content) / 2

    prob = 1
    for nt in seq:
        if (nt == 'A') | (nt=='T'):
            prob = prob * AT_freq
        elif (nt == 'G') | (nt=='C'):
            prob = prob * GC_freq
        else:
            raise ValueError
    prob_arr.append(round(np.log10(prob),3))

print(*prob_arr, sep = ' ')
