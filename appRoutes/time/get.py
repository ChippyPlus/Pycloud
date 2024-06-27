import json
import os
import sys

sys.path.insert(0, os.getcwd())
from resources.counter import counter

from flask import Blueprint, jsonify

bp = Blueprint('time get', __name__)


@bp.route(f'/time/get', methods=['GET'])
def add():
    return jsonify({"message": counter.get()}),200
