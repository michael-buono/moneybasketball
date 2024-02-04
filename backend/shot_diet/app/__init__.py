from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application object
app = Flask(__name__)

# Configure the application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shot_diet.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy database object
db = SQLAlchemy(app)


migrate = Migrate(app, db)

# For jupyter
app.extensions["sqlalchemy"] = db

# for react frontend to connect to flask
CORS(app)

# Import and register the blueprints or routes
from shot_diet.app import routes