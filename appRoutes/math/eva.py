from flask import Blueprint, jsonify, request
from shared import basicArithmetic
mathType = "eva"
bp = Blueprint(f'{mathType}', __name__)


@bp.route(f'/math/{mathType}', methods=['POST'])
def eva():
    basicArithmetic(request=request, jsonify=jsonify,mathType=mathType)
