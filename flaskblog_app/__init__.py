from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

flaskblog=Flask(__name__)
flaskblog.config['SECRET_KEY']="bad021b759edb72292003fafbe02264e"
flaskblog.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(flaskblog)
bcrypt=Bcrypt(flaskblog)
login_manager=LoginManager(flaskblog)
login_manager.login_view="login"
login_manager.login_message_category="info"

from flaskblog_app import routes