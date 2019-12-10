from modules.funcs import read_fasta

file = '/Volumes/KatahdinHD/Downloads/rosalind_grph.txt'

data_dict= read_fasta(file)

fasta_IDs = list(data_dict.keys())
x=3

prefix, suffix = zip(*[(val[:x], val[-x:]) for val in data_dict.values()])
suffix
prefix


for i, suf in enumerate(suffix):

    for j, pre in enumerate(prefix):
        s = fasta_IDs[i]
        p = fasta_IDs[j]


        if s == p:
            continue
        elif suf == pre:
            print(s, p)
