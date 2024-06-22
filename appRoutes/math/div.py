from flask import Blueprint, jsonify, request
from shared import basicArithmetic
mathType = "div"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def div():
    basicArithmetic(request=request, jsonify=jsonify,mathType=mathType)
