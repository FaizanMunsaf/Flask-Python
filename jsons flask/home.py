# -*- coding: utf-8 -*-

from flask import Flask,request
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def product():
    json_data = request.get_json()
    return json_data


# =============================================================================
#     if request.method == 'POST':
#         return "Your data has been submitted ! "
#     else:
#         json_data = request.get_json()
#         return json_data
# =============================================================================



if __name__ == "__main__":
    app.run(debug=True)