import os

from flask import Blueprint, jsonify, request, send_file
from os.path import basename
from shared import testAuth

bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


# sets the route to "/{parent dir}/{filename}"
@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['GET'])
def createFile():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.json:
        return jsonify({'error': 'Missing arg1'}), 400  # path in bucket
    if "arg2" not in request.json:
        return jsonify({'error': 'Missing arg2'}), 400  # bucket

    if not os.path.exists(f"resources/storage/{str(request.json['arg2'])}"):
        return jsonify({"error": "Bucket not found not found"}), 404

    if not os.path.exists(f"resources/storage/{str(request.json['arg2'])}/{str(request.json['arg1'])}"):
        return jsonify({"error": "File path not found not found"}), 404
    return send_file(f"resources/storage/{str(request.json['arg2'])}/{str(request.json['arg1'])}")
