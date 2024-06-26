from flask import Blueprint, jsonify, request
from shared import basicArithmetic

mathType = "mod"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def mod():
    return basicArithmetic(request=request, jsonify=jsonify, mathType=mathType)
