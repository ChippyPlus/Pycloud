import os.path
from src.main.commanFunctions.common.testAuth import testAuth
from src.main.commanFunctions.flaskRelated.getFlaskPath import buildRoutes
from flask import Blueprint, request

bp = Blueprint(str(__file__).removesuffix('.py'), __name__)




@bp.route(buildRoutes(file=__file__), methods=['POST'])
def function():
    AuthTest = testAuth(str(request.authorization))
    if AuthTest is not None:
        return AuthTest
    del AuthTest

