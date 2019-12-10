from modules.funcs import read_fasta

file = '/Volumes/KatahdinHD/Downloads/rosalind_tran.txt'

fasta_dict = read_fasta(file)

fasta_list = list(fasta_dict.keys())

s1 = fasta_dict[fasta_list[0]]
s2 = fasta_dict[fasta_list[1]]

aligned=list(zip(s1,s2))

transitions, transversions = 0,0
for pair in aligned:
    if pair[0] == pair[1]:
        print(pair)

    elif ((pair[0] in 'AG') & (pair[1] in 'AG')) | ((pair[0] in 'CT') & (pair[1] in 'CT')):
        print("Transition: {}".format(pair))
        transitions += 1
    elif ((pair[0] in 'AT') & (pair[1] in 'AT')) | ((pair[0] in 'CG') & (pair[1] in 'CG')):
        print("Transversion: {}".format(pair))
        transversions += 1
    elif ((pair[0] in 'AC') & (pair[1] in 'AC')) | ((pair[0] in 'GT') & (pair[1] in 'GT')):
        print("Transversion: {}".format(pair))
        transversions += 1

    else:
        print("bloop {}".format(pair))
        # raise Exception("Unknown base type")

print(transitions/transversions)
