from app import db
from werkzeug.security import generate_password_hash, check_password_hash
#The class below is the one that allows for users to be remembered in session data
from datetime import datetime


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64), index=True, unique=False)
    country_code = db.Column(db.String(64), index=True, unique=False)
