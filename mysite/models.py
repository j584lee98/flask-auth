from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(200), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  first_name = db.Column(db.String(200), nullable=False)
  last_name = db.Column(db.String(200), nullable=False)
  todos = db.relationship('Todo')

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  todo = db.Column(db.String(500), nullable=False)
  date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)