from shot_diet.app.services.team_service import get_or_fetch_teams
from flask import Blueprint, current_app, jsonify
from sqlalchemy import text

bp = Blueprint("main", __name__)


@bp.route("/api/test")
def index():
    return jsonify({"message": "Hello, world!"})


@bp.route("/api/healthz")
def healthz():
    try:
        # Access db through current_app's app context
        db_engine = current_app.extensions["sqlalchemy"].db.engine
        with db_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            # If we can execute this query, the database is up
            return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500


@bp.route("/api/teams")
def teams():
    team_hash = get_or_fetch_teams()
    return jsonify(team_hash), 200
