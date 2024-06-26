from flask import Blueprint, jsonify, request, send_file
from os.path import basename
from shared import testAuth

bp = Blueprint(str(basename(__file__).replace('.py', '')), __name__)


@bp.route(f"/{str(__file__.replace('.py', '').split('/')[-2])}/{str(__file__.replace('.py', '').split('/')[-1])}",
          methods=['GET'])
def function():
    if not testAuth(str(request.authorization)):
        return jsonify({'error': 'Unauthorized'}), 401
    where = "THIS AN ERROR"
    files = request.files
    for file in files.items():
        print(file)
        file[1].save(f"resources/storage/{file[0]}/{file[1].filename}")
        where = f"{file[0]}/{file[1].filename}"
    return jsonify({"message": f"Uploaded {where}"}), 200
