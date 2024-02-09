from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
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
    elif environment == "docker_development":
        logger.info("Setting up development database")
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@db/{os.getenv('MYSQL_DATABASE')}?charset=utf8mb4"
        )
    # For things like flask shell, we dont want to depend on having the docker environment running
    # Ensure you have created the database `moneybasketball_test` in your local mysql database
    # and have started it with something like `brew services start mysql`
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "mysql+pymysql://root@127.0.0.1/moneybasketball_test?charset=utf8mb4"
        )

    db.init_app(app)

    # Import models to ensure they're registered with SQLAlchemy
    from shot_diet.app.models import Player  # noqa: E402, F401

    # Initialize Flask migrate, CORS, and setup our routes
    Migrate(app, db)
    domain = os.getenv("ORIGIN_DOMAIN", "localhost")
    CORS(app, resources={r"/api/*": {"origins": domain}})
    app.register_blueprint(bp)

    # API rate limiting
    Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=["400 per day", "100 per hour"],
    )
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
