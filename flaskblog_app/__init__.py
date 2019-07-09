from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

flaskblog=Flask(__name__)
flaskblog.config['SECRET_KEY']="bad021b759edb72292003fafbe02264e"
flaskblog.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(flaskblog)
bcrypt=Bcrypt(flaskblog)

from flaskblog_app import routes