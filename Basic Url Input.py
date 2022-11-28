# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:02:59 2022

@author: Faizan
"""
from flask import Flask, request
app = Flask(__name__)


@app.route('/home')
def home():
    name = request.args.get('name')
    return f'My name is : {name}'


if __name__ == "__main__":
    app.run(debug=False)
