from flask import Flask
from threading import Thread
from sys import path
from os import getcwd

path.insert(0, getcwd())

from routes.math import add, sub, mul, div, mod, pow

from routes.time import get
from resources.timeKeeper import count

from routes.storage import download, upload,createbucket

app = Flask("Pycloud")

storageEndpoints = (download, upload,createbucket)
mathEndpoints = (add, sub, mul, div, mod, pow)
timeEndpoints = (get,)

for endpoint in storageEndpoints:
    app.register_blueprint(endpoint.bp)
    print(f"[LOADED] storage/{endpoint.__name__.split('.')[-1]}")

for endpoint in mathEndpoints:
    app.register_blueprint(endpoint.bp)
    print(f"[LOADED] math/{endpoint.__name__.split('.')[-1]}")
for endpoint in timeEndpoints:
    app.register_blueprint(endpoint.bp)
    print(f"[LOADED] time/{endpoint.__name__.split('.')[-1]}")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    counterThread = Thread(target=count, daemon=True)
    counterThread.start()
    app.run(debug=True, port=8080, host="0.0.0.0")
