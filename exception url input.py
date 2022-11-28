from flask import Flask, request
app = Flask(__name__)


@app.route('/home')
def product():
    try:
        username = request.args['username']
        return f'My name is : {username}'
    except:
        return "please enter your name"


if __name__ == "__main__":
    app.run(debug=False)
