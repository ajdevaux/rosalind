file = 'codon_table.txt'
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

def rna_to_protein(rna_str, codon_dict):
    rna_len = len(rna_str)
    if rna_len % 3 == 0:
        print("This sequence is divisible by 3")
    else:
        print("This sequence is NOT divisible by 3")

    prot_seq = ''
    codon_list = [rna_str[i:i+3] for i in range(0, len(rna_str),3)]
    for codon in codon_list:
        print(codon)
        if codon_dict[codon] != 'Stop':
            prot_seq = prot_seq + codon_dict[codon]
        else:
            break
    return prot_seq
