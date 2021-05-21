import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv
from flask_login import LoginManager

load_dotenv(find_dotenv())

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRES_URI']
  db.init_app(app)

  migrate = Migrate(app, db)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')

  from .models import User, Todo

  with app.app_context():
    db.create_all()

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  return app