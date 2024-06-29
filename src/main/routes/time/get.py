from resources.timeKeeper import counter
from src.main.commanFunctions.flaskRelated.getFlaskPath import buildRoutes
from flask import Blueprint, jsonify, request
from src.main.commanFunctions.common.testAuth import testAuth

bp = Blueprint(str(__file__).removesuffix('.py'), __name__)


@bp.route(buildRoutes(file=__file__), methods=['GET'])
def function():
    AuthTest = testAuth(str(request.authorization))
    if AuthTest is not None:
        return AuthTest
    del AuthTest
    return jsonify({"message": counter.get()}), 200
