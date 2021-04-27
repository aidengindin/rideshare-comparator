import flask
from flask import request

import asyncio
import datetime
import json
import random
import requests
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

# Main function to respond to client requests
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
        return json.dumps(generateError("Query did not contain all required arguments")), 400, {"Content-Type": "application/json"}

    response = asyncio.run(build_response(srclat, srclon, destlat, destlon))
    return json.dumps(response), {"Content-Type": "application/json"}

# Build a response to send to the client
# asynchronously waiting for external APIs
async def build_response(srclat, srclon, destlat, destlon):
    response = {}
    response["is-above-avg"] = False
    response["results"] = {}
    response["path"] = await get_route(srclat, srclon, destlat, destlon)
    return response

# Test if any argument is equal to None
def isAnyNone(*argv):
    for arg in argv:
        if arg == None:
            return True
    return False

# Generate an error JSON response
def generateError(reason):
    return {
        "reasons": [
            {
                "language": "en",
                "message": reason
            }
        ]
    }

# Get route data from MapQuest
async def get_route(srclat, srclon, destlat, destlon):
    keyfile = open("mapquest-key", "r")
    key = keyfile.read()
    keyfile.close()

    response = requests.get("http://www.mapquestapi.com/directions/v2/route?key={}&from={}&to={}".format(key, locstring(srclat, srclon), locstring(destlat, destlon)))
    if response.ok:
        return response.json()
    return generateError("MapQuest API responded with an error: " + response.reason)

# Get available rides from Uber
# Since we don't currently have Uber API access, this just generates dummy data
async def get_uber_rides(srclat, srclon, destlat, destlon):
    return [
        {
            "provider": "Uber",
            "name": "UberX",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(15, 25),
            "seats": 4,
            "shared": False
        },
        {
            "provider": "Uber",
            "name": "UberXL",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(25, 35),
            "seats": 6,
            "shared": False
        },
        {
            "provider": "Uber",
            "name": "Uber Pool",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(5, 15),
            "seats": 4,
            "shared": True
        }
    ]

# Get available rides from Lyft
# Since we don't currently have Uber API access, this just generates dummy data
async def get_uber_rides(srclat, srclon, destlat, destlon):
    return [
        {
            "provider": "Lyft",
            "name": "Lyft",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(15, 25),
            "seats": 3,
            "shared": False
        },
        {
            "provider": "Lyft",
            "name": "Lyft XL",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(25, 35),
            "seats": 5,
            "shared": False
        },
        {
            "provider": "Lyft",
            "name": "Lyft Shared",
            "pickup": random_time_in_range(5, 10),
            "arrival": random_time_in_range(15, 30),
            "price": random.randrange(5, 15),
            "seats": 4,
            "shared": True
        }
    ]

# Convert a lat/lon pair to a string
def locstring(lat, lon):
    return str(lat) + "," + str(lon)

# Choose a time uniformly at random between (current time + start_offset) and (current_time + end_offset)
# Offsets are specified in minutes
def random_time_in_range(start_offset, end_offset):
    offset = datetime.timedelta(seconds=(random.randrange(start_offset, end_offset) * 60))
    return datetime.datetime.now() + offset

if __name__ == "__main__":
    app.run(port=PORT, ssl_context=None)
