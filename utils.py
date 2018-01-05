import json

response_codes = {"not_found": 404, "invalid": 403, "ok": 200}


def generate_error(message, code):
    err = json.dumps({"error": message})
    return err, response_codes[code]
