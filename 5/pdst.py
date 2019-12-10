import numpy as np
from modules.funcs import read_fasta

def measure_p_dist(seqs):
    p_dist = []
    for s in seqs:
        s1,s2 = s
        mismatch_ct = 0
        slen = len(s1)
        if slen != len(s2):
            print("ERROR")
        else:
            for i in range(0,slen):
                if s1[i] != s2[i]:
                    mismatch_ct += 1
            p_dist.append(format(mismatch_ct / slen, '.4f'))

    return p_dist


def pdst():

    file ='/Volumes/KatahdinHD/Downloads/rosalind_pdst.txt'

    data_dict = read_fasta(file)
    seq_ct = len(data_dict)
    seq_list = list(data_dict.values())

    seqs =  [(s1, seq_list[j]) for j in range(0,len(seq_list)) for s1 in seq_list]

    p_dist = measure_p_dist(seqs)
    print(p_dist)
    error_array = np.asarray(p_dist, dtype=str).reshape(seq_ct,seq_ct)

    print('\n'.join(' '.join(cell for cell in row) for row in error_array))

if __name__ == "__main__":
    pdst()
