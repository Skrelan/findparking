from flask import Flask, request
import json
import logging
import models
import utils

VERSION = "v0.01"

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] | [%(levelname)s] | %(message)s")

app = Flask(__name__)

store = [models.Parking(1.0, 1.0), models.Parking(-1.0, -1.0)]


@app.route('/health', methods=["GET", "POST", "PUT", "DELETE"])
def health():
    response = json.dumps({"Server running, version": VERSION})
    return response


@app.route('/api/spots', methods=["GET"])
def show_me_parking():
    try:
        lat, lng, radius = request.args.get('lat'), request.args.get(
            'lng'), request.args.get('radius')
        user = models.User(lat, lng, radius)
        response = json.dumps({
            "User location":
            str(user.location.lat) + " | " + str(user.location.lng),
            "Radius":
            str(user.radius)
        })
        return response
    except Exception as e:
        err = "Request made w/o lat, lng and/or radius parameter"
        logging.error("{0}|{1}".format(err, e))
        return utils.generate_error(err, "invalid")


if __name__ == '__main__':
    app.run()
