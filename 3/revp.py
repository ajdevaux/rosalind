def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

def reverse_complement(string):
    if len(string) == 0:
        return string
    else:
        revstring = reverse(string)
        revstring = revstring.replace("A","t").replace("G","c").replace("T","a").replace("C",'g')

        return revstring

def revp():
    file = '/Volumes/KatahdinHD/Downloads/rosalind_revp.txt'
    with open(file, 'r') as f:
        data = f.readlines()

    dna = ''.join([s.strip('\n') for s in data if not s.startswith('>')])

    dna_len = len(dna)
    for start in range(0,dna_len,1):
        if (dna_len - start) < 4:
            break
        for length in range(4,13):
            end = start + length

            substr = dna[start:end]
            if length > len(substr):
                break
            revsub = reverse_complement(substr)

            if substr == revsub.upper():
                # print(substr, revsub)
                print(start+1, length)

if __name__ == "__main__":
    revp()
