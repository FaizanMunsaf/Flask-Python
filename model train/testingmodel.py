# -*- coding: utf-8 -*-
import pickle
from fastnumbers import isfloat

filename = "fruit_model"

loaded_model = pickle.load(open(filename, "rb"))

load = loaded_model.predict([[69.2]])

hello = input("Please Enter the value => ")

print(hello)

if isfloat(hello):
    value = float(hello)
else:
    value = "Value error"
    
print(value)
loaded_model.predict([[69.2]])
print(load)