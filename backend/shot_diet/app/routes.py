from shot_diet.app.services.team_service import get_or_fetch_teams
from flask import Blueprint, current_app, jsonify, request, abort
from sqlalchemy import text

bp = Blueprint("main", __name__)


def ajax_required(f):
    def wrapped(*args, **kwargs):
        if request.headers.get("X-Requested-With") != "XMLHttpRequest":
            abort(403)  # Forbidden access if the header doesn't match
        return f(*args, **kwargs)

    wrapped.__name__ = f.__name__
    return wrapped


@bp.route("/api/test")
@ajax_required
def index():
    return jsonify({"message": "Hello, world!"})


@bp.route("/api/healthz")
@ajax_required
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
@ajax_required
def teams():
    team_list = get_or_fetch_teams()
    team_list.sort()
    return jsonify(teams=team_list), 200
