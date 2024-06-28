from flask import Flask

app = Flask("Pycloud")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
