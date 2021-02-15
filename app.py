from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from data import babbys
import subprocess

# initialize app
app = Flask(__name__)
app.config[ "DEBUG" ] = True
# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///babbys.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db model
class Babby(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    size = db.Column(db.String(20), nullable=False)

    def __init__(self, **kwargs):
        super(Babby, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.name

# import routes
exec(open("./routes.py").read())