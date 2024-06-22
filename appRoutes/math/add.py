from flask import Blueprint, jsonify, request
from shared import basicArithmetic
mathType = "add"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def add():
    return basicArithmetic(request=request, jsonify=jsonify,mathType=mathType)
