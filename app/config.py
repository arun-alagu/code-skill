from os import environ, path
from dotenv import load_dotenv
from mongoengine import connect
# from flask_debugtoolbar import DebugToolbarExtension

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask config variables."""

    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")
    
    TESTING = True

    # DEBUG_TB_PANELS = 'flask_mongoengine.panels.MongoDebugPanel'
