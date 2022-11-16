import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sqlite3.db')
app.config['SECRET_KEY'] = 'a really really really really long secret key'

db = SQLAlchemy(app)
db.init_app(app)
