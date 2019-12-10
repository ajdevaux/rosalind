import re

fasta_file = '/Volumes/KatahdinHD/Downloads/rosalind_cons.txt'

def read_fasta(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
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

def find_motif(dna, m):
    motif = r'(?={})'.format(m)
    matches = re.finditer(motif, dna)

    return [x.start()+1 for x in matches]



list = find_motif(dna,m)
