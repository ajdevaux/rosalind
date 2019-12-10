import re

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
    match_locs = re.finditer(motif, dna)

    return [x.start()+1 for x in match_locs]


def rna_to_protein(rna_str, codon_dict):
    rna_len = len(rna_str)
    if rna_len % 3 == 0:
        print("This sequence is divisible by 3")
        pass
    else:
        print("This sequence is NOT divisible by 3")
        pass
    prot_seq = ''
    codon_list = [rna_str[i:i+3] for i in range(0, len(rna_str),3)]
    for codon in codon_list:
        print(codon)
        if len(codon) % 3 != 0:
            break
        elif codon_dict[codon] == 'Stop':
            prot_seq = prot_seq
            break
        else:
            prot_seq = prot_seq + codon_dict[codon]
            print(codon_dict[codon])
    return prot_seq
#===========================================================================#
fasta_dict=read_fasta('/Volumes/KatahdinHD/Downloads/rosalind_splc (1).txt')
# fasta_dict=read_fasta('../splc_test.txt')
codon_dict=read_codon_table('/Volumes/KatahdinHD/ResilioSync/DATA/pydata/rosalind/codon_table.txt')

str_list = list(fasta_dict.values())

dna_str = str_list[0]
for i in str_list[1:]:
    print(len(dna_str))
    intron_locs = find_motif(dna_str, i)[0]

    print(i, len(i), intron_locs)

    # for intron in sorted(intron_locs, reverse=True):
    end_intron = intron_locs + len(i)
    print(dna_str[intron_locs-1:end_intron-1])
    print(dna_str[0:intron_locs-1])
    print(dna_str[end_intron-1:])
    dna_str = dna_str[0:intron_locs-1] + dna_str[end_intron-1:]
    # print(dna_str)

mrna_spliced = dna_str.replace('T','U')

protein = rna_to_protein(mrna_spliced, codon_dict)

print(protein)
