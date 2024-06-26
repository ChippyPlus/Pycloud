import os
import sys

from flask import Flask, render_template, send_from_directory, request
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

# crypt imports

import appRoutes.crypt.passcode
# noinspection PyProtectedMember
import appRoutes.crypt._rsa
import appRoutes.crypt.fernet

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

# noinspection PyProtectedMember
app.register_blueprint(appRoutes.crypt._rsa.bp)
app.register_blueprint(appRoutes.crypt.fernet.bp)
app.register_blueprint(appRoutes.crypt.passcode.bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/down')
def down():
    return send_from_directory(".", "test", as_attachment=True)


@app.route("/up", methods=["POST"])
def upload_file():

    uploaded_file = request.files.get("test.localhost.txt")
    print(uploaded_file)
    if uploaded_file:
        filename = uploaded_file.filename
        uploaded_file.save(filename)
        return f"File {filename} uploaded successfully!"
    else:
        return "No file uploaded!", 400
