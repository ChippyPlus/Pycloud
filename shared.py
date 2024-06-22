import json


def testAuth(bearerToken: str):
    with open("resources/auth/users.json") as f:
        tokens = json.load(f)
        for token in tokens:
            if bearerToken == token["bearerToken"]:
                return True
        return False
