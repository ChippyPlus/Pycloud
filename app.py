from flask import Flask
import appRoutes.math.add
app = Flask("pi-cloud!")

app.register_blueprint(appRoutes.math.add.math_index_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
    return 'Hello World2!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
