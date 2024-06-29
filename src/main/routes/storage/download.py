import os.path
from src.main.commanFunctions.common.testAuth import testAuth
from src.main.commanFunctions.flaskRelated.getFlaskPath import buildRoutes
from flask import Blueprint, request, send_file, jsonify

bp = Blueprint(str(__file__).removesuffix('.py'), __name__)


@bp.route(buildRoutes(file=__file__), methods=['POST'])
def function():
    AuthTest = testAuth(str(request.authorization))
    if AuthTest is not None:
        return AuthTest
    del AuthTest

    if not os.path.exists(f"resources/storage/{str(request.json['arg2'])}"):
        return jsonify({"error": "Bucket not found not found"}), 404

    if not os.path.exists(f"resources/storage/{str(request.json['arg2'])}/{str(request.json['arg1'])}"):
        return jsonify({"error": "File path not found not found"}), 404
    return send_file(f"resources/storage/{str(request.json['arg2'])}/{str(request.json['arg1'])}"), 200
