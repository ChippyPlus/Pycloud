import os
import sys

from flask import Flask, render_template, send_from_directory, request
sys.path.insert(0,os.getcwd())

# math imports
import appRoutes.math.add
import appRoutes.math.sub
import appRoutes.math.mul
import appRoutes.math.div
import appRoutes.math.pow
import appRoutes.math.mod
import appRoutes.math.eva

# storage imports
import appRoutes.storage.createbucket
import appRoutes.storage.download
import appRoutes.storage.upload
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

app.register_blueprint(appRoutes.storage.createbucket.bp)
app.register_blueprint(appRoutes.storage.download.bp)
app.register_blueprint(appRoutes.storage.upload.bp)
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


if __name__== "__main__":
    app.run()