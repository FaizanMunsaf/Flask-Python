# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 00:15:53 2022

@author: Faizan
"""

from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Token')

@auth.verify_token
def verify_token(token):
        return '1234567890abcdefg' == token

@app.route('/', methods=["GET","POST"])
@auth.login_required
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)