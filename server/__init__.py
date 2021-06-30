from flask import Flask, request, jsonify
from server.utils import get_response


app = Flask(__name__)


@app.post("/api/")
def check_image():
    json_data = request.get_json()
    return jsonify(get_response(json_data))
