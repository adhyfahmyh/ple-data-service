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
        print(request.json)
        print(request.data)
        save.save_activity_log()
        return "Saved"


if __name__ == "__main__":
    app.run(debug=True)
