from flask import Flask, request
import json
import logging
import models
import utils
import logic

VERSION = "v0.01"

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] | [%(levelname)s] | %(message)s")

app = Flask(__name__)

store = {
    "SOMA": models.Parking(1.0, 1.0),
    "4th & Kings": models.Parking(-1.0, -1.0),
    "SAP Stadium": models.Parking(-11.0, -11.0)
}


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
        response = logic.find_parking(user, store)
        return utils.generate_response(response, "ok", "Parking found")
    except Exception as e:
        err = "Request made w/o lat, lng and/or radius parameter"
        logging.error("{0} | {1}".format(err, e))
        return utils.generate_error(err, "invalid")


@app.route('/api/spots', methods=["POST"])
def block_my_parking():
    try:
        parking_name = request.args.get('name')
        if parking_name not in store:
            return utils.generate_error("This parking doesn't exsist",
                                        "not found")
        if store[parking_name].taken:
            return utils.generate_error("This parking is already taken", "ok")
        store[parking_name].taken = True
        return utils.generate_response("success", "ok",
                                       "Parking has been reserved")
    except Exception as e:
        err = "Request made w/o name"
        logging.error("{0} | {1}".format(err, e))
        return utils.generate_error(err, "invalid")


if __name__ == '__main__':
    app.run()
