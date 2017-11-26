from flask_sqlalchemy import SQLAlchemy

from weather.app import app

db = SQLAlchemy(app)
