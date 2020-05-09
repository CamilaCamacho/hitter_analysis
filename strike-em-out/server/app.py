
from flask import Flask, jsonify
from flask_cors import CORS
# from flask_mongoengine import MongoEngine
from flask import Flask, request, Response
from db import initialize_db
#from models import batters

COURSES = [
    {
        'title': 'Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript ',
        'author': 'David Herman',
        'paperback': True
    },
    {
        'title': 'JavaScript: The Good Parts',
        'author': 'Douglas Crockford',
        'paperback': False
    },
    {
        'title': 'Eloquent JavaScript: A Modern Introduction to Programming',
        'author': 'Marijn Haverbeke',
        'paperback': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {
    # name of db
    'db': 'sixBatters',
    # momo's host address
    'host': '192.168.1.89',
    # default port used
    'port': 27017
}
#initialize the database
initialize_db(app)


# enable CORS
# needed to make cross-origin AJAX requests possible
# this is resource specific CORS
# r'/*' to r'/api/*'
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
# @cross_origin() # this allows CORS on a given route
def ping_pong():
    return jsonify('pong')


@app.route('/courses', methods=['GET'])
def all_courses():
    return jsonify({
        'status': 'success',
        'courses': COURSES
    })

#momo added this for testing sixbatters db
@app.route('/strikeemout')
def get_batters():
    Batters = batters.objects()
    return Response(Batters, mimetype="application/json", status=200)

# #momo added this for testing sixbatters db
@app.route('/strikeemout', methods=['GET'])
def push_pitchtype():
    #body = request.get_json()
    # Batters = batters(**body).save()
    pitch_type = Batters.pitch_type
    return {'pitch_type': str(pitch_type)}, 200


@app.route('/strikeemout', methods=['GET'])
def strikeemout():
    return jsonify('Strike Out!')


if __name__ == '__main__':
    app.run()
