import rsa
from flask import Blueprint, jsonify, request
from os.path import basename
from shared import testAuth

bp = Blueprint("rsa", __name__)


@bp.route(f"/crypt/rsa", methods=["POST"])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.json:  # message
        return jsonify({'error': 'Missing `arg1`'}), 400

    publicKey, privateKey = rsa.newkeys(512)
    message = str(request.json["arg1"])
    encMessage = rsa.encrypt(message.encode(),
                             publicKey)
    return jsonify({'message': str(encMessage).removeprefix("b'")}), 200
