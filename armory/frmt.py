from Bio import Entrez
def parse_fasta(data):
    fasta_ct = 0
    seq_data =''
    ID_list = []
    fasta_dict = {}
    for line in data:
        line = line.strip('\n')
        print(line)
        if line.startswith('>'):
            seq_data=''
            line = line.strip('>')
            fasta_dict[line] = ''
            ID_list.append(line)
            fasta_ct += 1
        else:
            seq_data = seq_data + line
            fasta_ID = ID_list[fasta_ct-1]
            fasta_dict[fasta_ID] = seq_data

    return fasta_dict

with open('/Volumes/KatahdinHD/Downloads/rosalind_frmt.txt', 'r') as f:

    query = [line.strip("\n") for line in f]

query
# query=["FJ817486, JX069768, JX469983"]
main_handle = Entrez.efetch(db="nucleotide", id=query, rettype='fasta')
main_record = main_handle.read()
fasta_dict = parse_fasta(main_record.split("\n"))

shortest_str = min([len(v) for k,v in fasta_dict.items()])

for k,v in fasta_dict.items():
    if len(v) == shortest_str:
        print(">"+k+"\n"+v)
        
