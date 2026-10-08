from flask import Flask, render_template, jsonify, request
from typing import Any
#from . import create_app

#app=create_app()
app= Flask(__name__)

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

dice=[
    {"numberOfSides":6},
    {"numberOfSides":20}
]

@app.route("/api/dice", methods=["GET","POST"])
def handle_dice_requests():
    #GET method handling, if a user requests information we will display the json of dice
    if request.method=="GET":
        return jsonify(available_dice=dice)
    #POST request handling, if a user posts something, we will update the dice json
    else:
        try:
            payload=request.json
            if not payload["numberOfSides"]:
                raise Exception()
            if not payload["numberOfSides"]>1:
                raise Exception()
            new_dice={"numberOfSides":payload["numberOfSides"]}
            if new_dice in dice:
                raise Exception()
            dice.append(new_dice)
            return {"message":"dice created"}, 201 # returns a tuple indicating success, a message and a status code for Flask, without a status code Flask returns 200 which means OK, 201 means a new resource was successfully created
        except:
            return {"message":"An unknown error occured"}, 500 # code 500 means an error occured internal server error

@app.route("/api/sample2")
def return_sample_json2():
    return jsonify(foo="bar")

if __name__ == "__main__":
    app.run(port=5000)