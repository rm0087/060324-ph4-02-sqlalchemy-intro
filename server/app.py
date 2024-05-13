#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db # ADD OTHER MODELS HERE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)


# ROUTES


@app.get('/')
def index():
    return { "stuff": "I am stuff" }, 404


# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)
