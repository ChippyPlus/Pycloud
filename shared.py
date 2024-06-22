import json


def testAuth(bearerToken: str):
    bearerToken = bearerToken.removeprefix('Bearer ')
    with open("resources/auth/users.json") as f:
        tokens = json.load(f)
        for token in tokens:
            if bearerToken == token:
                return True
        return False
