from flask import Blueprint, jsonify, request
from shared import testAuth
from resources import constants

bp = Blueprint("new", __name__)


@bp.route(f"/admin/new", methods=['POST'])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    currentP = "ERROR"
    with open(f"{constants.authDir}/users.json", 'r') as f:
        import json
        jsonData: dict = json.load(f)
        currentP = jsonData[str(request.authorization).removeprefix("Bearer ")]["privileges"]
    mandatoryArgs = ["arg1", "arg2", "arg3"]
    # arg1 name
    # arg2 privilege
    # arg3 password

    for arg in mandatoryArgs:
        if arg not in request.json:
            return jsonify({'error': 'Missing ' + arg}), 400
    if currentP < request.json["arg2"]:
        return jsonify({'error': 'Missing permission'}), 403

    if request.json["arg3"] in jsonData:
        return jsonify({'error': 'Must have unique passwords try again'}), 409

    jsonData[request.json["arg3"]] = {
        "name": request.json["arg1"],
        "privileges": request.json["arg2"],
        "id": jsonData[[i for i in jsonData.keys()][-1]]["id"] + 1
    }
    with open(f"{constants.authDir}/users.json", 'w') as f:
        json.dump(jsonData, f,indent=4)

    return jsonify({"message": "User created"}), 201
