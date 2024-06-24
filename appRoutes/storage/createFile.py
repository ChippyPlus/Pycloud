import os.path

from flask import Response
from flask import Blueprint, jsonify, request
from os.path import basename
import resources.constants as constants
from shared import testAuth

bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['POST'])
def createFile():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg2" not in request.json:
        return jsonify({'error': 'Missing "bucket" parameter'}), 400
    if "arg1" not in request.json:
        return jsonify({'error': 'Missing "path" parameter'}), 400

    bucket = request.json['arg2']
    path = request.json['arg1']
    if not os.path.exists(f"{constants.storageDir}/{bucket}"):
        return jsonify({'error': 'bucket does not exist'}), 404

    if os.path.exists(f"{constants.storageDir}/{bucket}/{path}"):
        return jsonify({'error': 'File already exists'}), 409

    if "/" in path:
        return jsonify({'error': 'No sub directory\'s in a file'}), 400

    try:
        with open(f"{constants.storageDir}/{bucket}/{path}", "w") as f:
            f.write("")
    except NotADirectoryError:
        return jsonify({'error': 'arg1 is not a directory'}), 404

    return Response("File created", 201)
