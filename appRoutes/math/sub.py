from flask import Blueprint, jsonify, request
from shared import basicArithmetic

mathType = "sub"
bp: Blueprint = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def sub():
    return basicArithmetic(request=request, jsonify=jsonify, mathType=mathType)
