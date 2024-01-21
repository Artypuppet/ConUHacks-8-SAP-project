from flask import Flask, request, jsonify
from flask_cors import CORS
from BackEndOld.main import Driver
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
        filePath = os.path.join("uploadFiles", file.filename)
        file.save(filePath)
        print("got the file")
    graphData, FinalMetrics = Driver(filePath)
    return jsonify(graphData=graphData, finalMetrics=FinalMetrics)


if __name__ == '__main__':
    app.run()
