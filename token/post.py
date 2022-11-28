# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 00:29:57 2022

@author: Faizan
"""
import requests


# =============================================================================
# data1= requests.get('https://www.google.com/')
# data1.status_code
# data1.text
# =============================================================================

headers= { 'Authorization' : 'Token hakjhfkajhkfkjj' }

data2= requests.post('http://127.0.0.1:5000/model?predict=6.9',headers=headers)
data2.status_code
data2.text
