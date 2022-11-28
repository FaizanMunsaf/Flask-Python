# -*- coding: utf-8 -*-

import requests

dict1 = {
  "Id": 78912,
  "Customer": "Jason Sweet",
  "Quantity": 1,
  "Price": 18.00}

response1 = requests.post("http://127.0.0.1:5000", json=dict1)
print(response1.text)

response2 = requests.get("http://127.0.0.1:5000",json=dict1 )
print(response2.text)




