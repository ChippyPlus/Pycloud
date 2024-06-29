import os.path
from flask import Response
from flask import Blueprint, jsonify, request
from os.path import basename

from src.main.commanFunctions.common.testAuth import testAuth

# Sets the blueprint name to the filename
bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


# sets the route to "/{parent dir}/{filename}"
@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['POST'])
def createFile():
    AuthTest = testAuth(str(request.authorization))
    if AuthTest is not None:
        return AuthTest
    del AuthTest

    if "arg1" not in request.json:
        return jsonify({'error': 'Missing "bucket" parameter'}), 400

    bucket = request.json['arg1']

    if "/" in bucket:  # To keep no subdirectories in the buckets
        return jsonify({'error': 'No sub directory\'s in a bucket'}), 400

    try:
        os.mkdir(f"resources/storage/{bucket}")
        del bucket
    except FileExistsError:
        return jsonify({'error': 'File already exists'}), 409
    return Response("Bucket created", 201)
