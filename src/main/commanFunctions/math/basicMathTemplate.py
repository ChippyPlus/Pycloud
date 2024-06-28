from flask import Request, jsonify
from src.main.commanFunctions.flaskRelated.findArg import findArg
from src.main.liveData.mathMemos import MathMemos

def basicMathTemplate(mathType: str, request: Request):
    """
    does an operation on 2 numbers `arg1` and `arg2` in the json on `request in order`
    """
    if not findArg(("arg1", "arg2"), request, MustReturn=False):
        return findArg(("arg1", "arg2"), request, MustReturn=True)

    arg1 = request.json['arg1']
    arg2 = request.json['arg2']

    if mathType == "add":

        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "sub":
        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "mul":
        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "div":
        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "pow":
        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "mod":
        return jsonify({"message": arg1 + arg2}), 200
    else:
        return jsonify(
            {
                "error": "and this is an error, from having a unknown math type please give reproduction tips if found"}), 400
