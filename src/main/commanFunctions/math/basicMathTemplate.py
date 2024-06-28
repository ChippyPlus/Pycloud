from time import ctime

from flask import jsonify
from src.main.commanFunctions.math.memoify import memoize


@memoize
def basicMathTemplate(mathType: str, args: dict[str, int]):
    """
    does an operation on 2 numbers `arg1` and `arg2` in the json on `request in order`
    """
    if "arg1" not in args: return jsonify({"error": "Missing `arg1`"}), 400
    if "arg2" not in args: return jsonify({"error": "Missing `arg2`"}), 400
    arg1 = args["arg1"]
    arg2 = args["arg2"]
    with open("logs/tasks.log", "a") as f:  # log to tasks
        f.write(f"{ctime()} [MATH] EXECUTED,  | {mathType} {args}\n")
    if mathType == "add":
        return jsonify({"message": arg1 + arg2}), 200
    elif mathType == "sub":
        return jsonify({"message": arg1 - arg2}), 200
    elif mathType == "mul":
        return jsonify({"message": arg1 * arg2}), 200
    elif mathType == "div":
        return jsonify({"message": arg1 / arg2}), 200
    elif mathType == "pow":
        return jsonify({"message": arg1 ** arg2}), 200
    elif mathType == "mod":
        return jsonify({"message": arg1 % arg2}), 200
    else:
        return jsonify(
            {
                "error": "and this is an error, from having a unknown math type please give reproduction tips if found"}
        ), 400
