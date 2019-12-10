from Bio import Entrez


with open('/Volumes/KatahdinHD/Downloads/rosalind_gbk.txt', 'r') as f:

    query = [line.strip("\n") for line in f]

query

main_handle = Entrez.esearch(db="nucleotide", term=query[0]+'[Organism]', datetype='pdat',
                             mindate=query[1], maxdate=query[2],
                             retmax='100000'
)
main_record = Entrez.read(main_handle)


for k,v in main_record.items():
    print(k,v)

total_IDs = int(main_record['Count'])

print(total_IDs)
