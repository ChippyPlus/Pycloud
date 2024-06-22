from flask import Blueprint, jsonify, request
from shared import basicArithmetic
mathType = "sub"
math_index_bp = Blueprint(f'{mathType}', __name__)


@math_index_bp.route(f'/math/{mathType}', methods=['POST'])
def sub():
    basicArithmetic(request=request, jsonify=jsonify,mathType=mathType)
