#!/usr/bin/env python3

from flask import request
from config import app, db
# from models import MODELS GO HERE


# ROUTES

@app.get('/')
def index():
    return { "response": "hello world" }, 200


# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)