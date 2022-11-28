# -*- coding: utf-8 -*-

from flask import Flask, request
app = Flask(__name__)


@app.route('/home')
def product():
    username = request.args['username']
    return f'My name is : {username}'


if __name__ == "__main__":
    app.run(debug=False)
