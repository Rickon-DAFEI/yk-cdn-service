from flask import Flask, request, jsonify, send_file
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/uploads", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    # 保存上传的文件，可以根据需要修改保存路径
    file.save(os.path.join("uploads", file.filename))

    return jsonify({"message": "File uploaded successfully"})


@app.route("/uploads/<path:filename>")
def serve_file(filename):
    # 拼接文件路径，可以根据需要修改文件存储位置
    file_path = "uploads/" + filename

    try:
        return send_file(file_path)
    except FileNotFoundError:
        return f"File {filename} not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
