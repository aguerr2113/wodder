from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '8531f7bbd6b2d053ce3eb682fc716ebf'
db = SQLAlchemy(app)

from wodder import routes

