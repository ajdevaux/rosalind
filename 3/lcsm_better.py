
def parse_fasta(data):
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
            seq_data = seq_data + line
            fasta_ID = ID_list[fasta_ct-1]
            fasta_dict[fasta_ID] = seq_data

    return fasta_dict

def read_fasta(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
    fasta_dict = parse_fasta(data)

    return fasta_dict

def common_substr(seq_0, seqs, length):
    # look at all possible substrings of a given 'length'
    for start in range(len(seq_0) - length + 1):

        part = seq_0[start:start+length]

        # as soon as you find a sequence that doesn't contain this substring move on to the next substring
        # otherwise return this substring
        # note: indicates that there is at least one common substring of this length
        for seq in seqs:
            if part not in seq:
                break
        else:
            return part
    return ""

def lcsm():

    fasta_file = '/Volumes/KatahdinHD/Downloads/rosalind_gc.txt'

    fasta_dict = read_fasta(fasta_file)

    # fasta_IDs = tuple(fasta_dict.keys())
    seqs = list(fasta_dict.values())
    # pop seq_0 to reduce number of sequences to search and eliminate need to re-extract each time
    seq_0 = seqs.pop(0)

    ## starting points for the bounds on the longest common substring used in the binary search ##
    left = 0
    # +1 added to allow entire sequence to be the longest common substring
    right = len(seq_0) + 1

    # repeat until left and right are adjacent
    #     use left + 1, because you've already eliminated the right most and you get an endless loop otherwise ...
    while left + 1 < right:
        print(left)    # pick midpoint in lengths -- nb:  assumes integer math
        mid = (left + right) // 2
        print(mid)

        # if any substring of length mid is common to all sequences
        #    look for substrings of this length or longer
        # otherwise look for substrings of this length or less
        if common_substr(seq_0, seqs, mid) != "":
            left = mid
        else:
            right = mid

    print("\n"+common_substr(seq_0, seqs, left)+"\n")



if __name__ == "__main__":
    lcsm()
