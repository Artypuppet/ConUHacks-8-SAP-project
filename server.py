from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
CORS(app)


@app.route('/files', methods=["Get", "POST"])
def postCSVFile():
    print(request)
    if 'file' not in request.files:
        print("Not in request.files")
    file = request.files['file']
    if file.filename == '':
        print("No selected file")
    if request.method == "POST":
        file.save(os.path.join("uploadFiles", file.filename))
        print(file.filename)
        print(os.path.join("./uploadFiles", secure_filename(file.filename)))
        print(file)
        print("got the file")
    return {}


if __name__ == '__main__':
    app.run()
