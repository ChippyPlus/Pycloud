from flask import Flask

# math imports
import appRoutes.math.add
import appRoutes.math.sub
import appRoutes.math.mul
import appRoutes.math.div
import appRoutes.math.pow
import appRoutes.math.mod
import appRoutes.math.eva



app = Flask("pi-cloud!")

app.register_blueprint(appRoutes.math.add.math_index_bp)



@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
    return 'Hello World2!'

