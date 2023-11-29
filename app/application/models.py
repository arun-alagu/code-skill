from flask_mongoengine.wtf import model_form
from . import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin,db.Document):
    email = db.StringField(required=True)
    password = db.StringField(required=True)

    def set_password(self,password):
        """ Create hashed password."""
        self.password=generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self,password):
        """ Check hashed password."""
        return check_password_hash(self.password,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)