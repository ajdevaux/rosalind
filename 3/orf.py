import re

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

def read_codon_table(file):
    with open(file, 'r') as f:
        data = f.read()
        data= data.replace('\n', ',')
        data=data.replace('      ', ',')
        data=data.replace('   ', ',')


    data = data.split(',')

    codon_dict = {}
    for item in data:
        if item is not '':
            datapair = item.split(' ')
            codon_dict[datapair[0]] = datapair[1]
    return codon_dict


def find_motif(string, m):
    motif = r'(?={})'.format(m)
    match_locs = re.finditer(motif, string)

    return [x.start()+1 for x in match_locs]

def complement(string):
    comp_str = ''
    for n in string:
        if n == 'A':
            comp_str = comp_str + 'T'
        elif n == 'T':
            comp_str = comp_str + 'A'
        elif n == 'C':
            comp_str = comp_str + 'G'
        elif n == 'G':
            comp_str = comp_str + 'C'
    return comp_str

def rna_to_protein(rna_str, codon_dict):
    rna_len = len(rna_str)
    if rna_len % 3 == 0:
        # print("This sequence is divisible by 3")
        pass
    else:
        # print("This sequence is NOT divisible by 3")
        pass
    prot_seq = ''
    codon_list = [rna_str[i:i+3] for i in range(0, len(rna_str),3)]
    for codon in codon_list:
        # print(codon)
        if len(codon) % 3 != 0:
            break
        elif codon_dict[codon] == 'Stop':
            prot_seq = prot_seq + '+'
            break
        else:
            prot_seq = prot_seq + codon_dict[codon]
    return prot_seq


fasta_file = '/Volumes/KatahdinHD/Downloads/rosalind_orf (2).txt'
fasta_dict = read_fasta(fasta_file)

codon_file = 'codon_table.txt'
codon_dict = read_codon_table(codon_file)

fasta_ID, dna = fasta_dict.popitem()

c_dna = complement(dna[::-1])

rna = dna.replace('T','U')
c_rna = c_dna.replace('T','U')

start_codons_fwd = find_motif(rna, 'AUG')
start_codons_rev = find_motif(c_rna, 'AUG')


prot_fwd = [rna_to_protein(rna[val-1:], codon_dict) for val in start_codons_fwd]
prot_rev = [rna_to_protein(c_rna[val-1:], codon_dict) for val in start_codons_rev]
total_protein = (prot_fwd + prot_rev)

prot_set= set([val.strip('+') for val in total_protein if val.endswith('+')])
for val in prot_set:
    print(val)
