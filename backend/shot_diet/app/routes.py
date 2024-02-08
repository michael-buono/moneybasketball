from flask import jsonify
from flask import Blueprint
from sqlalchemy import text
from shot_diet import app

bp = Blueprint("main", __name__)


@bp.route("/api/test")
def index():
    return jsonify({"message": "Hello, world!"})


@bp.route("/api/healthz")
def healthz():
    with app.app.app_context():
        try:
            app.db.session.execute(text("SELECT 1"))
            return jsonify({"message": "\n\n----------- Connection successful !')"})
        except Exception:
            return jsonify({"message": "\n\n----------- Connection FAILED !"})
