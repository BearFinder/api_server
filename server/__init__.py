from flask import Flask, request, jsonify
from server.utils import get_response


app = Flask(__name__)


@app.route("/api/", methods=["POST"])
def check_image():
    json_data = request.get_json()
    code, response = get_response(json_data)
    return jsonify(response), code
