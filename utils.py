import json

response_codes = {"not_found": 404, "invalid": 403, "ok": 200}


def generate_error(message, code):
    err = json.dumps({"error": message})
    return err, response_codes[code]


def generate_response(payload, code, message):
    resp = json.dumps({"payload": payload, "message": message})
    return resp, response_codes[code]
