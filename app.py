from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."


# 연습할 발음 입력
@app.route("/upload-clear-speech", methods=["POST"])
def upload_clear_speech():
    if not request.files:  # 입력된 파일이 없으면
        return "No file part in the request", 400
    for key in request.files:  # 입력된 파일이 있으면
        audio_file = request.files[key]
        if audio_file.filename == "":  # 파일 명이
            return f"No selected file for key: {key}", 400
        # Save the file or process it here
        audio_file.save(f"clear_speech/{audio_file.filename}")
        return f"File {audio_file.filename} uploaded successfully with key {key}", 200


# 연습할 발음 입력
@app.route("/upload-practice-speech", methods=["POST"])
def upload_practice_speech():
    if not request.files:  # 입력된 파일이 없으면
        return "No file part in the request", 400
    for key in request.files:  # 입력된 파일이 있으면
        audio_file = request.files[key]
        if audio_file.filename == "":  # 파일 명이
            return f"No selected file for key: {key}", 400
        # Save the file or process it here
        audio_file.save(f"practice_speech/{audio_file.filename}")
        return f"File {audio_file.filename} uploaded successfully with key {key}", 200


if __name__ == "__main__":
    app.run(debug=True, port=3000)
