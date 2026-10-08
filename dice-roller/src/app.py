from flask import Flask, render_template

app= Flask(__name__)

@app.route("/") #allows you to define where the app should route to when the defined url is set, in this case the root "/" leads to the defined hello_world
@app.route("/<string:name>") # you can specifiy the data type to receive by setting the type in the route
def hello_world(name:str = None):
    return render_template("hello2.html",_name=name)

#@app.route("/<name>")
#def personalised_hello(name):
    #return render_template("hello.html", _name=name)  #allows you to route to a personalized page that receives a variable


if __name__ == "__main__":
    app.run(debug=True, port=5000)