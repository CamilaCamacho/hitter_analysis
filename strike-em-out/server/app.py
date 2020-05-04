
from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

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
    'db': 'sixBatters',
    'host': '192.168.1.89',
    'port': 27017
}
db = MongoEngine(app)

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


@app.route('/strikeemout', methods=['GET'])
def strikeemout():
    return jsonify('Strike Out!')


if __name__ == '__main__':
    app.run()
