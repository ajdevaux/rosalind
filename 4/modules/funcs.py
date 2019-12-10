import pandas as pd
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


def seq_profiler(seq_df):
    profile_df = pd.DataFrame(data=None, columns= ['A','G','T','C'])
    for ix, row in seq_df.iterrows():
        As,Cs,Gs,Ts=0,0,0,0
        for val in row:
            if val is 'A':
                As += 1
            elif val is 'C':
                Cs +=1
            elif val is 'G':
                Gs += 1
            elif val is 'T':
                Ts += 1
            else:
                raise ValueError
        profile_df = profile_df.append({'A':As, 'C':Cs, 'G':Gs, 'T':Ts}, ignore_index=True).astype('int')

    return profile_df
