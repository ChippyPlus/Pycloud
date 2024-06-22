from flask import Blueprint, jsonify, request
from shared import basicArithmetic
mathType = "pow"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def pow():
    basicArithmetic(request=request, jsonify=jsonify,mathType=mathType)
