import flask
from flask import request

import json
import sys

PORT = 5000    # port to run the server on
DEBUG = False  # whether to run in debug mode

if "--debug" in sys.argv:
    DEBUG = True

app = flask.Flask(__name__)
app.config["DEBUG"] = DEBUG

@app.route("/", methods=["GET"])
def home():
    response = {}
    response["is-above-avg"] = False
    response["results"] = {}
    response["path"] = {}
    
    return json.dumps(response), {"Content-Type": "application/json"}

if __name__ == "__main__":
    app.run(port=PORT, ssl_context="adhoc")
