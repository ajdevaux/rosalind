import re
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

def read_fasta(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
    fasta_dict = parse_fasta(data)

    return fasta_dict

def find_motif(string, m):
    motif = r'(?={})'.format(m)
    match_locs = re.finditer(motif, string)

    return [x.start()+1 for x in match_locs]

def lcsm():
    fasta_file = '/Volumes/KatahdinHD/Downloads/rosalind_lcsm (1).txt'

    fasta_dict = read_fasta(fasta_file)

    fasta_IDs = tuple(fasta_dict.keys())

    seq1 = fasta_dict[fasta_IDs[0]]

    longest_len = 350

    string_set = set([seq1[start:start + length]
                      for length in range(2,longest_len)
                      for start in range(0,len(seq1),1)]
    )
    string_set = sorted(string_set, key=len, reverse=True)

    for ID in fasta_IDs[1:]:
        seq = fasta_dict[ID]
        for substr in string_set.copy():

            locs = find_motif(seq, substr)
            if not locs == []:
                break
            else:
                print("not {}".format(substr))
                string_set.remove(substr)
        print(len(string_set))

    lcs = max(string_set, key=len)
    print("\n{}\n".format(lcs))
    print(len(lcs))


        # match_dict[substr] =  locs

if __name__ == "__main__":
    lcsm()
