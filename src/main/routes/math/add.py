import os.path
from os import getcwd
from sys import path

path.insert(0, getcwd())
from src.main.commanFunctions.flaskRelated.getFlaskPath import buildRoutes
from flask import Blueprint, request
from src.main.commanFunctions.math.basicMathTemplate import basicMathTemplate

bp = Blueprint(str(__file__).removesuffix('.py'), __name__)


@bp.route(buildRoutes(file=__file__), methods=['POST'])
def function():
    return basicMathTemplate(
        str(os.path.basename(__file__).removesuffix(".py")),
        request.json,
        str(request.authorization)
    )
