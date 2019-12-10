file = '/Volumes/KatahdinHD/Downloads/rosalind_hamm.txt'

with open(file, 'r') as f:
    data = list(f.readlines())
s,t = data

def dH(s,t):
    hamm_dist = 0
    for x in range(0,len(s)-1):
        if s[x] != t[x]:
            hamm_dist += 1


    return hamm_dist

dH(s,t)
