from flask import Blueprint, jsonify, request
from shared import testAuth
math_index_bp = Blueprint('add', __name__)


@math_index_bp.route('/math/add', methods=['POST'])
def add():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    jsonBody = request.get_json()
    if "arg1" not in jsonBody:
        return jsonify({"error": "Missing `arg1`"}), 400
    if "arg2" not in jsonBody:
        return jsonify({"error": "Missing `arg2`"}), 400

    result = int(jsonBody["arg1"]) + int(jsonBody["arg2"])

    return jsonify({"message": result}), 200
