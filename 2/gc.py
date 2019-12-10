file = '/Volumes/KatahdinHD/Downloads/rosalind_gc (1).txt'

def read_fasta(fasta_file):
    with open(fasta_file, 'r') as file:
        data = list(file.readlines())
        fasta_ct = 0
        seq_data =''
        ID_list = []
        fasta_dict = {}
        for line in data:

            line = line.strip('\n')
            if line.startswith('>'):
                seq_data=''
                line = line.strip('>')
                fasta_dict[line] = ''
                ID_list.append(line)
                fasta_ct += 1
            else:
                seq_data= seq_data + line
                fasta_ID = ID_list[fasta_ct-1]
                fasta_dict[fasta_ID] = seq_data
    return fasta_dict


fasta_dict = read_fasta(file)

for fasta, seq in fasta_dict.items():
    Gct = seq.count('G')
    Cct = seq.count('C')
    perc_GC = ((Gct + Cct) /len(seq))*100
    print(fasta+'\n', round(perc_GC,6))
