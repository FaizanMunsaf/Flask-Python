# -*- coding: utf-8 -*-

import requests


dict1 = {"status": "200",
         "input": "df90",
         "message": "Data is fine"}
    


headers= { 'Authorization' : 'Token hakjhfkajhkfkjj' }

# Through URL
response1 = requests.post("http://127.0.0.1:5000/model?predict=10f0",headers = headers)
print(response1.text)


# Withjsons
response1 = requests.post("http://127.0.0.1:5000/model", json=dict1, headers = headers)
print(response1.text)
a= response1.text
b= response1.json()


# Error
response1 = requests.post("http://127.0.0.1:5000/model", headers = headers)
print(response1.text)



# =============================================================================
# data2= requests.post('http://127.0.0.1:5000/model?predict=6.9', headers=headers)
# data2.status_code
# data2.text
# =============================================================================
