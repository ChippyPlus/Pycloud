from flask import Blueprint, jsonify, request
from shared import testAuth

bp = Blueprint("new", __name__)

@bp.route(f"/test0000", methods=['POST'])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify({"Test": "Test"})
