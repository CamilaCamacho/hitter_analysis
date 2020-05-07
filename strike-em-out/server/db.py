# Here we have imported MongoEngine
# created the db object
# defined a function initialize_db()
# which we are gonna call from our app.py
# to initialize the database.

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

# app = Flask(__name__)
# app.config.from_object(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'sixBatters',
#     'host': '192.168.1.89',
#     'port': 27017
# }
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
