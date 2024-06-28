import os
import sys
import threading
from resources.counter import counter, count

sys.path.insert(0, os.getcwd())
from flask import Flask, jsonify

# time imports
import appRoutes.time.get
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

# administrator imports
import appRoutes.admin.new

sys.set_int_max_str_digits(2147483647)

app = Flask("py-cloud!")
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
app.register_blueprint(appRoutes.time.get.bp)
app.register_blueprint(appRoutes.admin.new.bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    counterThread = threading.Thread(target=count, daemon=True)
    counterThread.start()
    app.run("0.0.0.0", 8080, debug=True)
