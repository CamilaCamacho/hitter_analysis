
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
# from flask_mongoengine import MongoEngine
from flask import Flask, request, Response
from flask_pymongo import PyMongo
from db import initialize_db
#from models import batters

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017") # connects to client locally
db_using = client["season2019"] # get the database
main_collection = db_using["battingData"] # get the collection
team_collection = db_using["teamPlayerId"] # get the connection
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


# print("success1")
# @app.route('/ping', methods=['GET'])
# # @cross_origin() # this allows CORS on a given route
# def ping_pong():
#     event = main_collection.find_one({'game_pk': 566551})
#     name = event['pitcher_name']
#     return jsonify(name)
#     #return jsonify(name = name)

print("success1")
@app.route('/strikeemout', methods=['GET'])
# @cross_origin() # this allows CORS on a given route
def get_team_names():
    team_name = []
    for item in team_collection.find():
        team_name.append(item['mlb_team_long'])
    return jsonify(team_name)

@app.route('/courses', methods=['GET'])
def all_courses():
    return jsonify({
        'status': 'success',
        'courses': COURSES
    })

@app.route('/strikeemout', methods=['GET'])
def strikeemout():
    return jsonify('Strike Out!')


if __name__ == '__main__':
    app.run()
