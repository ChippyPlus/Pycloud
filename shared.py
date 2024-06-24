import json
import resources.constants as constants

def testAuth(bearerToken: str):
    bearerToken = bearerToken.removeprefix('Bearer ')
    with open(f"{constants.authDir}/users.json") as f:
        tokens = json.load(f)
        for token in tokens:
            if bearerToken == token:
                return True
        return False


def basicArithmetic(request, jsonify, mathType):
    if mathType not in ["add", "sub", "mul", "div", "pow", "mod", "eva"]:
        return "bra!"

    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    jsonBody = request.get_json()
    if "arg1" not in jsonBody:
        return jsonify({"error": "Missing `arg1`"}), 400
    if mathType != "eva":
        if "arg2" not in jsonBody:
            return jsonify({"error": "Missing `arg2`"}), 400

    if mathType == "add":
        result = int(jsonBody["arg1"]) + int(jsonBody["arg2"])
    elif mathType == "sub":
        result = int(jsonBody["arg1"]) - int(jsonBody["arg2"])
    elif mathType == "mul":
        result = int(jsonBody["arg1"]) * int(jsonBody["arg2"])
    elif mathType == "div":
        result = int(jsonBody["arg1"]) / int(jsonBody["arg2"])
    elif mathType == "pow":
        result = int(jsonBody["arg1"]) ** int(jsonBody["arg2"])
    elif mathType == "mod":
        result = int(jsonBody["arg1"]) % int(jsonBody["arg2"])
    elif mathType == "eva":
        result = int(eval(jsonBody["arg1"]))
    else:
        result = "bra!2"
    return jsonify({"message": result}), 200
