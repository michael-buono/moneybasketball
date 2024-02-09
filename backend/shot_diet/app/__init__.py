from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import logging
from google.cloud.sql.connector import Connector, IPTypes
import os
from shot_diet.database import db
from .routes import bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    # Create the Flask application object
    app = Flask(__name__)
    environment = os.getenv("FLASK_ENV", "development")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if environment == "production":
        connector = Connector(IPTypes.PRIVATE)

        # Python Connector database connection function
        def getconn():
            return connector.connect(
                os.getenv("DB_CONNECTION"),  # Cloud SQL Instance Connection Name
                "pymysql",
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD"),
                db=os.getenv("DB_NAME"),
                ip_type=IPTypes.PRIVATE,  # IPTypes.PRIVATE for private IP
            )

        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"creator": getconn}
    else:
        logger.info("Setting up development database")
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "mysql+pymysql://moneybasketball:currywaydowntownbang@db/moneybasketball_test?charset=utf8mb4"
        )

    db.init_app(app)

    # Import models to ensure they're registered with SQLAlchemy
    from shot_diet.app.models import Player  # noqa: E402, F401

    # Initialize Flask migrate, CORS, and setup our routes
    Migrate(app, db)
    CORS(app)
    app.register_blueprint(bp)

    # Database initialization for local development,
    # Since we get a new db every time we run docker-compose up
    if environment == "development":
        with app.app_context():
            db.create_all()

    # Allow Flask's current_app to access the db
    app.extensions["sqlalchemy"] = db

    return app


# Return an instance of the app, as gunicorn cannot be passed a function
app = create_app()
