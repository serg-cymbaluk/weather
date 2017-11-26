"""
Database models
"""
from flask_login import UserMixin

from weather.app import login_manager
from weather.db import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Temperature(db.Model):
    __tablename__ = 'temperature'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    min_value = db.Column(db.Integer)
    max_value = db.Column(db.Integer)
