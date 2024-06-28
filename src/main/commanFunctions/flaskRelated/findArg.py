from flask import Request


def findArg(flaskArgs: tuple, request: Request, MustReturn):  # TODO make faster
    if not MustReturn:
        for arg in flaskArgs:
            if arg not in request.json:
                return False
        return True
    else:
        for arg in flaskArgs:
            if arg not in request.json:
                return {"error": f"Argument `{arg}` not found"}, 400
        return None
