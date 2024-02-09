from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import logging
from google.cloud.sql.connector import Connector, IPTypes
import os
from shot_diet.database import db


# Python Connector database connection function
def getconn():
    conn = connector.connect(
        os.getenv("DB_CONNECTION"),  # Cloud SQL Instance Connection Name
        "pymysql",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        ip_type=IPTypes.PRIVATE,  # IPTypes.PRIVATE for private IP
    )
    return conn


# Create the Flask application object
app = Flask(__name__)

# Configure logging
logger = logging.getLogger(__name__)

environment = os.getenv("FLASK_ENV", "development")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Cloud SQL in production, local sqlite in dev
if environment == "production":
    connector = Connector(IPTypes.PRIVATE)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"creator": getconn}
    # Create the SQLAlchemy database object
    db.init_app(app)
    migrate = Migrate(app, db)
else:
    logger.info("Setting up development database")
    # app.config["SQLALCHEMY_DATABASE_URI"] = (
    #     "mysql+pymysql://root@127.0.0.1/moneybasketball_test?charset=utf8mb4"
    # )
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://moneybasketball:currywaydowntownbang@db/moneybasketball_test?charset=utf8mb4"
    )
    # Create the SQLAlchemy database object
    db.init_app(app)
    from shot_diet.app.models import Player  # noqa: E402, F401


    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()


# # Create the SQLAlchemy database object
# db.init_app(app)
from .routes import bp  # noqa: E402

app.register_blueprint(bp)  # noqa: F401


# migrate = Migrate(app, db)
app.extensions["sqlalchemy"] = db

# For flask migrate to pick up our models
from shot_diet.app.models import Player  # noqa: E402, F401

CORS(app)
