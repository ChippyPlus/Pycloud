from flask import Flask
from threading import Thread

from src.main.liveData.clock import count

app = Flask("Pycloud")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    counterThread = Thread(target=count, daemon=True)
    counterThread.start()
    app.run(debug=True, port=8080, host="0.0.0.0")
