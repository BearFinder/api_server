import configparser
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename


config = configparser.ConfigParser()
config.read("./config.ini")
model_file = config["MODEL"]["file"]


try:
    from detector import image_file, init
    init(model_file)
except ImportError:
    import subprocess
    subprocess.call("bash install.sh")
    from detector import image_file, init
    init("model.pth")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./src/"
app.config['MAX_CONTENT_PATH'] = 10000000

@app.route("/api/", methods=["POST"])
def check_image():
    f = request.files["upload_file"]
    filename = secure_filename(f.filename)
    save_file = "res/" + filename
    input_file = app.config["UPLOAD_FOLDER"] + filename
    f.save(input_file)
    image_file(input_file, save_file)
    return send_file(save_file)

app.run(debug=True)