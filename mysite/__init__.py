import os
import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URI')
  db.init_app(app)

  migrate = Migrate(app, db)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')

  from .models import User, Todo

  with app.app_context():
    db.create_all()

  return app