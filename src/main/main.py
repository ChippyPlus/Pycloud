from flask import Flask
from threading import Thread

from src.main.liveData.clock import count

from src.main.routes.math import add
from src.main.routes.math import sub
from src.main.routes.math import mul
from src.main.routes.math import div
from src.main.routes.math import mod
from src.main.routes.math import pow
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
