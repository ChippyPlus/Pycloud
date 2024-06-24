import sys

from flask import Flask, render_template
import markdown.extensions.fenced_code

# math imports
import appRoutes.math.add
import appRoutes.math.sub
import appRoutes.math.mul
import appRoutes.math.div
import appRoutes.math.pow
import appRoutes.math.mod
import appRoutes.math.eva

# storage imports
import appRoutes.storage.createBucket
import appRoutes.storage.createFile
sys.set_int_max_str_digits(2147483647)
app = Flask("pi-cloud!")

app.register_blueprint(appRoutes.math.add.bp)
app.register_blueprint(appRoutes.math.sub.bp)
app.register_blueprint(appRoutes.math.mul.bp)
app.register_blueprint(appRoutes.math.div.bp)
app.register_blueprint(appRoutes.math.pow.bp)
app.register_blueprint(appRoutes.math.mod.bp)
app.register_blueprint(appRoutes.math.eva.bp)

app.register_blueprint(appRoutes.storage.createBucket.bp)
app.register_blueprint(appRoutes.storage.createFile.bp)

@app.route('/')
def hello_world():
    return 'Hello World!'
