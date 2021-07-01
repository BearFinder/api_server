from flask import Flask, request, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./src/"
app.config['MAX_CONTENT_PATH'] = 10000000

@app.route("/api/", methods=["POST"])
def check_image():
    f = request.files["upload_file"]
    filename = app.config["UPLOAD_FOLDER"] + secure_filename(f.filename)
    f.save(filename)
    return send_file(filename)
