import requests

import re

query_list = ['Q08DA1']

for query in query_list:

    params = {'query':query, 'format':'tab', 'columns':'go'}

    uniprot_resp = requests.get("https://www.uniprot.org/uniprot/", params=params)

    data = uniprot_resp.text

list_data = re.split(r"[\n;]", data)

for val in list_data:
    start = val.find('[')
    if start != -1:
        result = val[:start].strip()
        print(result)
