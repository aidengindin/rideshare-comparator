import flask
from flask import request

import json
import sys

PORT = 5000         # port to run the server on
DEBUG = False       # whether to run in debug mode
SSL_CONTEXT = None  # indicates whether to use HTTPS

if "--debug" in sys.argv:
    DEBUG = True

if "--https" in sys.argv:
    SSL_CONTEXT = "ahdoc"

app = flask.Flask(__name__)
app.config["DEBUG"] = DEBUG

@app.route("/", methods=["GET"])
def home():
    query = request.args
    
    srclat = srclon = destlat = destlon = None
    if "srclat" in query:
        srclat = query["srclat"]
    if "srclon" in query:
        srclon = query["srclon"]
    if "destlat" in query:
        destlat = query["destlat"]
    if "destlon" in query:
        destlon = query["destlon"]

    # return an error if the query doesn't contain the required parameters
    if isAnyNone(srclat, srclon, destlat, destlon):
        return json.dumps(generateError("Query did not contain all required arguments")), {"Content-Type": "application/json"}

    response = {}
    response["is-above-avg"] = False
    response["results"] = {}
    response["path"] = {}
    
    return json.dumps(response), {"Content-Type": "application/json"}

# Test if any argument is equal to None
def isAnyNone(*argv):
    for arg in argv:
        if arg == None:
            return True
    return False

# Generate an error JSON response of the form:
# {
#     "reaons:" [
#         {
#             "language": "en",
#             "message": reason
#         }
#     ]
# }
def generateError(reason):
    response = {}
    response["reasons"] = []
    response["reasons"].append({})
    response["reasons"][0]["message"] = "en"
    response["reasons"][0]["message"] = reason

    return response

if __name__ == "__main__":
    app.run(port=PORT, ssl_context=None)
