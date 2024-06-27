import os.path
from flask import Response
from flask import Blueprint, jsonify, request
from os.path import basename
import resources.constants as constants
from shared import testAuth

# Sets the blueprint name to the filename
bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


# sets the route to "/{parent dir}/{filename}"
@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['POST'])
def createFile():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.json:
        return jsonify({'error': 'Missing "bucket" parameter'}), 400

    bucket = request.json['arg1']

    if "/" in bucket:  # To keep no subdirectories in the buckets
        return jsonify({'error': 'No sub directory\'s in a bucket'}), 400

    try:
        os.mkdir(f"{constants.storageDir}/{bucket}")
    except FileExistsError:
        return jsonify({'error': 'File already exists'}), 409
    return Response("Bucket created", 201)
