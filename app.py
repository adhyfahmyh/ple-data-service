from flask import Flask, request, json
import save
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Index"


@app.route("/save_activity_log", methods=["POST"])
def save_activity_log():
    if request.method == "POST":
        data = request.json

        save.save_activity_log(
            data["username"], data["shortlink"], data["datetime"])
        return "Saved"


@app.route("/close_activity_log", methods=["POST"])
def close_activity_log():
    if request.method == "POST":
        data = request.json

        save.save_close_date_activity(
            data["username"], data["shortlink"], data["datetime"])
        return "Closed"


@app.route("/save_bookmark", methods=["POST"])
def save_bookmark():
    if request.method == "POST":
        data = request.json

        save.save_bookmark(data["username"], data["shortlink"])
        return "Bookmarked"


@app.route("/remove_bookmark", methods=["POST"])
def remove_bookmark():
    if request.method == "POST":
        data = request.json

        save.save_bookmark(data["username"], data["shortlink"])
        return "Unbookmarked"


if __name__ == "__main__":
    app.run()
