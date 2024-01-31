from shot_diet.app import app, db
from flask import render_template, jsonify

@app.route('/api/test')
def index():
    return jsonify({"message": "Hello, world!"})
