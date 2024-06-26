import os

from flask import Response
from flask import Blueprint, jsonify, request, send_file
from os.path import basename
import resources.constants as constants
from shared import testAuth

bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['GET'])
def createFile():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    if "arg1" not in request.args:
        return jsonify({'error': 'Missing arg1'}), 400  # path in bucket
    if "arg2" not in request:
        return jsonify({'error': 'Missing arg2'}), 400  # bucket

    if not os.path.exists(f"resources/storage/{str(request.args['arg1'])}"):
        return jsonify({"error": "Bucket not found not found"}), 404
    if not os.path.exists(f"resources/storage/{str(request.args['arg1'])}/{str(request.args['arg2'])}"):
        return jsonify({"error": "File not found not found"}), 404

    return send_file(f"resources/storage/{str(request.args['arg1'])}/{str(request.args['arg2'])}")

