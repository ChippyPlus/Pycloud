from flask import Flask
from threading import Thread
from liveData.clock import count
from routes.math import add
from routes.math import sub
from routes.math import mul
from routes.math import div
from routes.math import mod
from routes.math import pow
app = Flask("Pycloud")

mathEndpoints = [add, sub, mul, div, mod, pow]
for endpoint in mathEndpoints:
    app.register_blueprint(endpoint.bp)
    print(f"[LOADED] math/{endpoint.__name__.split('.')[-1]}")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    counterThread = Thread(target=count, daemon=True)
    counterThread.start()
    app.run(debug=True, port=8080, host="0.0.0.0")
