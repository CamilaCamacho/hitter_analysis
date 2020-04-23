from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instatiate the app
td_app = Flask(__name__)
td_app.config.from_object(__name__)

# enable CORS
# needed to make cross-origin AJAX requests posisble
# this is resource specific CORS
# 
# r'/*' to r'/api/*'
CORS(td_app, resources={r'/*':{'origins':'*'}})

# sanity check route
@td_app.route('/ping', methods=['GET'])
#@cross_origin() # this allows CORS on a givrn route
def pin_pong():
    return jsonify('pong')

if __name__ == '__main__':
    td_app.run()
