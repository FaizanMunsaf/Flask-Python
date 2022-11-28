# -*- coding: utf-8 -*-

from flask import Flask, request
import pickle
from fastnumbers import isfloat
from flask_httpauth import HTTPTokenAuth


app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Token')


filename = "fruit_model"

loaded_model = pickle.load(open(filename, "rb"))

def load_func(value):
    load = loaded_model.predict([[value]])

    dict1 = {"status": "200",
             "Prediction": load[0],
             "input": value,
             "message": "Data is fine"}

    return dict1

@auth.verify_token
def verify_token(token):
    return 'hakjhfkajhkfkjj' == token


@app.route('/model', methods=["GET", "POST"])
@auth.login_required
def product():
    try:

        prediction = request.args['predict']
        print(prediction)

        if isfloat(prediction) or prediction.isdigit():
            value = float(prediction)
        else:
            return "Value error"
        
        return load_func(value)

        
    except:
        
        try:
            json_data = request.get_json()
            data = json_data["input"]
            if isfloat(data) or data.isdigit():
                value = float(data)
            else:
                return "Value Error"
            
            return load_func(value)
        
        
        except :
            return "Data won't found ! "


@app.route('/')
def home():
    return "Please select the /model url above port"


if __name__ == "__main__":
    app.run(debug=True)
