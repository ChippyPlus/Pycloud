from json import load
from flask import jsonify
from time import ctime


def testAuth(brearToken: str):
    with open("resources/auth/users.json", 'r') as f:
        data = load(f)
    code = brearToken.removeprefix("Bearer ")

    if code not in data:
        with open("logs/auth.log", 'a') as f:
            f.write(f"{ctime()} [AUTH] denied | {code}\n")
        return jsonify({"error": "unauthorized"}), 401
    else:
        with open("logs/auth.log", 'a') as f:
            f.write(f"{ctime()} [AUTH] allowed | {code} | {data[code]['name']}\n")
        return None
