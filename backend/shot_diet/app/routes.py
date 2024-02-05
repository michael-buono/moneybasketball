from flask import jsonify
from flask import Blueprint

bp = Blueprint("main", __name__)


@bp.route("/api/test")
def index():
    return jsonify({"message": "Hello, world!"})
