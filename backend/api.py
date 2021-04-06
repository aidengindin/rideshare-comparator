import flask
import sys

PORT = 5000    # port to run the server on
DEBUG = False  # whether to run in debug mode

if "--debug" in sys.argv:
    DEBUG = True

app = flask.Flask(__name__)
app.config["DEBUG"] = DEBUG

@app.route("/", methods=["GET"])
def home():
    return "<p>This will return something useful later!"

if __name__ == "__main__":
    app.run(port=PORT)
