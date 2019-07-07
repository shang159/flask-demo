from flask import Flask
from flask_sqlalchemy import SQLAlchemy


flaskblog=Flask(__name__)
flaskblog.config['SECRET_KEY']="bad021b759edb72292003fafbe02264e"
flaskblog.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(flaskblog)


from flaskblog_app import routes