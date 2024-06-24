import base64
import hashlib
from cryptography.fernet import Fernet
from flask import Blueprint, jsonify, request
from os.path import basename
from shared import testAuth

bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['POST'])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.json:
        return jsonify({'error': 'Missing `arg1`'}), 400
    if "arg2" not in request.json:
        return jsonify({'error': 'Missing `arg2`'}), 400

    def mkKey(passcode: bytes) -> bytes:
        assert isinstance(passcode, bytes)
        hlib = hashlib.md5()
        hlib.update(passcode)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

    password = str(request.json['arg2'])
    key = mkKey(password.encode('utf-8'))
    fernet = Fernet(key)
    data_in = str(request.json['arg1'])
    cypher_text = fernet.encrypt(data_in.encode('utf-8'))

    return jsonify({'message': cypher_text}), 200
