import requests

from modules.funcs import find_motif

def mprt():
    query_list = ['A9QPL9','P03452','P19106', 'P06OF6']

    n_glyc = 'N[^P][ST][^P]'#N, followed by not P, followed by S or T, followed by not P

    for query in query_list:

        params = {'query':query, 'format':'fasta'}

        fasta_data = requests.get("https://www.uniprot.org/uniprot/", params=params)

        data_list = fasta_data.text.split("\n")

        prot_string = ''.join([s for s in data_list if not s.startswith('>')])

        loc_list = find_motif(prot_string, n_glyc)

        if not loc_list == []:
            print(query)
            print(prot_string)
            print(*loc_list, sep=' ')

if __name__ == '__main__':
    mprt()
