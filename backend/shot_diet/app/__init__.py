from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from .routes import bp
import os
from sqlalchemy import text

# Create the Flask application object
app = Flask(__name__)
app.register_blueprint(bp)

# Configure logging
logger = logging.getLogger(__name__)

environment = os.getenv("FLASK_ENV", "development")

# Cloud SQL in production, local sqlite in dev
if environment == "production":
    db_user = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_connection_name = os.getenv("DB_CONNECTION")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{db_user}:{db_password}@/{db_name}?unix_socket=/cloudsql/{db_connection_name}"
    )
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shot_diet.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# For jupyter
app.extensions["sqlalchemy"] = db

# Test DB connectivity
with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))
        print("\n\n----------- Database Connection successful !")
    except Exception as e:
        print("\n\n----------- Database Connection failed ! ERROR : ", e)

# for react frontend to connect to flask
CORS(app)
