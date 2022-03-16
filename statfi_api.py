"""
This file contains functions that can be utilized in Datafetcher 
This file is NOT going to be used in the final product
"""

from textwrap import indent
import requests
import json

from pathlib import Path

path = Path(__file__).parent / "request.json"

url = 'https://pxnet2.stat.fi/PXWeb/api/v1/en/ymp/taulukot/Kokodata.px'
payload = open(path)
payload = json.load(payload)

payload['query'][0]['selection']['values'] = ["Khk_yht_index"]
payload['query'][1]['selection']['values'] = [2014,2015]

payload = json.dumps(payload)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
res = requests.post(url, data=payload, headers=headers)

p = json.loads(res.text)
print(json.dumps(p, indent=4))
with open('STATFI_dummy.json', 'w') as outfile:
    json.dump(p, outfile)