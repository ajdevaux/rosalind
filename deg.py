file = '/Volumes/KatahdinHD/Downloads/rosalind_deg (2).txt'

with open(file, 'r+') as f:
    data = [line.rstrip('\n') for line in f]

# print(data)

verts, edges = map(lambda x: int(x), data.pop(0).split(' '))

# print(data)

data = list(map(lambda x:int(x),(' '.join(data)).split(' ')))

data
result = []
for i in range(1,1001):
    ct = data.count(i)
    # print(i, ct)
    if ct > 0:
        result.append(ct)

print(' '.join(map(lambda x: str(x), result)))
