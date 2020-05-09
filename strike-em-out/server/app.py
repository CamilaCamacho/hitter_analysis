
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
# from flask_mongoengine import MongoEngine
from flask import Flask, request, Response
from flask_pymongo import PyMongo
from db import initialize_db
#from models import batters

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017") # connects to client locally
dbUsing = client["sixBatters"] # get the database
collectionUse = dbUsing["batters"] # get the connection
#print(collectionUse.find_one({'game_pk': 566551}))
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     # name of db
#     'db': 'sixBatters',
#     # momo's host address
#     'host': '192.168.1.89',
#     # default port used
#     'port': 27017
# }
# #initialize the database
# initialize_db(app)

# enable CORS
# needed to make cross-origin AJAX requests possible
# this is resource specific CORS
# r'/*' to r'/api/*'
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
print("success1")
@app.route('/ping', methods=['GET'])
# @cross_origin() # this allows CORS on a given route
def ping_pong():
    event = collectionUse.find_one({'game_pk': 566551})
    name = event['pitcher_name']
    return jsonify(name)
    #return jsonify(name = name)

@app.route('/courses', methods=['GET'])
def all_courses():
    return jsonify({
        'status': 'success',
        'courses': COURSES
    })

#momo added this for testing sixbatters db
# @app.route('/ping')
# def get_batterName():
#     name = mongo.db.sixBatters.find({"pitcher_name": "Sam Selman"})
#     return render_template("index.html", name = name)
#
# #momo added this for testing sixbatters db
# @app.route('/ping', methods=['GET'])
# def get_batterNames():
#     #name = sixBatters.batters({pitcher_name: "Sam Selman"})
#     return jsonify("Momo")

# #momo added this for testing sixbatters db
# @app.route('/ping', methods=['GET'])
# def push_pitchtype():
#     #body = request.get_json()
#     # Batters = batters(**body).save()
#     pitch_type = Batters.pitch_type
#     return {'pitch_type': str(pitch_type)}, 200


@app.route('/strikeemout', methods=['GET'])
def strikeemout():
    return jsonify('Strike Out!')


if __name__ == '__main__':
    app.run()
