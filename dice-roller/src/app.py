from flask import Flask, render_template
from typing import Any

from . import create_app

from.api import dice

app=create_app()
#app= Flask(__name__)

def wrap_template_rendering(template_name:str, **context:Any):
    return render_template(template_name, _author="Rita", context=context)

@app.route("/hello") #allows you to define where the app should route to when the defined url is set, in this case the root "/" leads to the defined hello_world
@app.route("/hello/<string:name>") # you can specifiy the data type to receive by setting the type in the route
def hello_world(name:str = None):
    return wrap_template_rendering("hello2.html",_name=name)

#@app.route("/<name>")
#def personalised_hello(name):
    #return render_template("hello.html", _name=name)  #allows you to route to a personalized page that receives a variable

@app.route("/")
def home():
    return wrap_template_rendering("home.html")


@app.route("/dices")
def handle_dice():
    return wrap_template_rendering("dice.html")

#@app.route("/api/sample2")
#def return_sample_json2():
    #return jsonify(foo="bar")

if __name__ == "__main__":
    app.run(port=5000)