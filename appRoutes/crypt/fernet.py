from cryptography.fernet import Fernet
from flask import Blueprint, jsonify, request
from os.path import basename
from shared import testAuth

bp = Blueprint("fernet", __name__)


@bp.route(f"/crypt/fernet", methods=['POST'])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.json:
        return jsonify({'error': 'Missing `arg1`'}), 400
    message = str(request.json["arg1"])
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return jsonify({'message': str(encMessage).removeprefix("b'")}), 200
