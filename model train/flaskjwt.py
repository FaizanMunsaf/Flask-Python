# -*- coding: utf-8 -*-

from flask import Flask,request,session,make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = "JustDemonstrating"


def check_for_tokenn(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return {"message":"Missing token"},403
        token = request.args.get('token')
        if not token:
            return {"message" : "Missing token"},403
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
        
        except:
            return {"message":"Invalid token"},403
        return func(*args, **kwargs)
    return wrapped
        


@app.route("index")
def index():
    if not session.get("loged_in"):    
        return "You are logged in"
    else:
        return "Currently logged in"


@app.route("/public")
def public():
    return "Anyone can view this"

@app.route("/auth")
@check_for_tokenn
def authorised():
    return "This is only viewable with a token"


@app.route("/login",methods = ["POST"])
def login():
    if request.form["username"] and request.form['password'] == "password":
        session["logged_in"] = True
        token = jwt.encode({
            "user" : "Faizan Munsaf",
            "exp" : datetime.datetime.utcnow()+datetime.timedelta(seconds = 60)
            
            },
            app.config["SECRET_KEY"])
        return {"token" : token.decode("utf-8")}
    
    else:
        return make_response("Unable to verify",403,{"www-Authenticate": "Basic realm : login"})
        



if __name__ == "__main__":
    app.run()