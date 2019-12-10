from random import choice
from math import factorial

n = 89
k = 9

perm_ct = factorial(n)//factorial(n-k)

print(perm_ct % 1000000)


perm_set = set()

while len(perm_set) < perm_ct:
    new_perm = []
    int_list = list(range(1,n+1))
    while len(int_list) > 0:
        val = choice(int_list)
        int_list.remove(val)

        new_perm.append(str(val)+' ')

    perm_set.add(''.join(new_perm))


for val in perm_set:
    print(val)
