from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from os import environ, path
from dotenv import load_dotenv

db=MongoEngine()

def create_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')

  app.config['MONGODB_SETTINGS']={
        'db':'codeskill',
        'host':'127.0.0.1',
        'port':27017
    }
  app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
  db.init_app(app)
  toolbar = DebugToolbarExtension(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models import User

  @login_manager.user_loader
  def load_user(user_id):
      # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.objects(id=user_id).first()

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)
  
  return app