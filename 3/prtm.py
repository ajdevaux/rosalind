
#Just copy and paste the table into a 'txt' file and the code parses it.
file = 'monoisotopic_mass_table.txt'
with open(file, 'r') as f:
    data = f.read()
    data = data.replace('\n', ',')
mass_data=data.split(",")

mass_dict = {}
for item in mass_data:
    if item is not '':
        datapair = item.split('   ')
        mass_dict[datapair[0]] = float(datapair[1])

def protein_mass(prot_str, mass_dict=mass_dict):
    total_mass = 0
    print(prot_str)
    for aa in prot_str.upper():
        try:
            total_mass = total_mass + mass_dict[aa]
        except KeyError:
            print("Unrecognized amino acid symbol {}; skipping".format(aa))
            pass

    return round(total_mass,3)

#Run function on the string to get the answer.
#This will work with any string of text, btw.
