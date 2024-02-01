from flask import jsonify

from shot_diet.app import app


@app.route("/api/test")
def index():
    return jsonify({"message": "Hello, world!"})
