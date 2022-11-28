# -*- coding: utf-8 -*-

from flask import Flask, request


app = Flask(__name__)


@app.route('/calculator')
def product():
    firstnum = request.args['firstnumber']
    secondnum = request.args['secondnumber']

    if firstnum.isdigit() and secondnum.isdigit():
        a = int(firstnum)
        b = int(secondnum)

        if a > b:
            value = firstnum
        else:
            value = secondnum

    else:
        "Value error"

    Mul = a * b
    Sub = a - b
    Add = a + b
    Div = a / b

    dict = {"firstNo": a,
            "secondNo": b,
            "Multiplication": Mul,
            "Subtraction": Sub,
            "Addition": Add,
            "Divsion": Div,
            "greaterValue": value}

    return dict

# f'''First Value : {firstnum} & Second Value : {secondnum}
#        Addition = {Add}
#        Subtraction = {Sub}
#        Multiplication = {Mul}
#        Division = {Div}'''


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", ssl_context="adhoc")
