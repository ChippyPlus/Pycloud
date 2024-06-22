from flask import Flask

# math imports
import appRoutes.math.add

app = Flask("pi-cloud!")

app.register_blueprint(appRoutes.math.add.math_index_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
    return 'Hello World2!'

