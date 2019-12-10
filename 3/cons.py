import pandas as pd

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

def main():
    fasta_file = '/Volumes/KatahdinHD/Downloads/rosalind_cons.txt'
    fasta_dict = read_fasta(fasta_file)

    seq_df = pd.DataFrame()
    for k,seq in fasta_dict.items():
        seq_df[k] = list(seq)

    profile_df = seq_profiler(seq_df)

    profile_df.T.to_csv(r"/Volumes/KatahdinHD/ResilioSync/DATA/pydata/rosalind/consensus_profile.txt",
                        header=None, sep = ' ')

    consensus_string = ''.join(list(profile_df.idxmax(axis=1)))
    with open("/Volumes/KatahdinHD/ResilioSync/DATA/pydata/rosalind/consensus_result1.txt", 'w') as f:
        f.write(consensus_string +'\n')

if __name__ == "__main__":
    main()
