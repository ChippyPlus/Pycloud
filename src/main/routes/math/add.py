from src.main.commanFunctions.flaskRelated.getFlaskPath import buildRoutes
from flask import Blueprint, request
from src.main.commanFunctions.math.basicMathTemplate import basicMathTemplate

bp = Blueprint(str(__file__).removesuffix('.py'), __name__)


@bp.route(buildRoutes(file=__file__))
def function(): pass


class e(str):
    json = {
        "arg1": 10,
        # "arg2": 20
    }


f = e()

print(basicMathTemplate("add", f))
