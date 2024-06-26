from flask import Blueprint, jsonify, request
from shared import basicArithmetic

mathType = "mul"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def mul():
    return basicArithmetic(request=request, jsonify=jsonify, mathType=mathType)
