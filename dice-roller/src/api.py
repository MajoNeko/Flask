from flask import Blueprint, jsonify, request

api_bp= Blueprint("api", __name__)

dice=[
    {"numberOfSides":6},
    {"numberOfSides":20}
]


@api_bp.route("/dice", methods=["GET","POST"]) #TODO: split this into a GET and a POST method, consider handling more request types
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
