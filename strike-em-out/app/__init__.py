""" 
Flask Application Instance
Creates the application object as an intance of class Flask from flask package.
app package is defined by app directory and __init__.py script
app cariable is defined as instance of class Flask in __init__.py script; making it a member of app package
""" 
from flask import Flask

app = Flask(__name__)
# __name__ is Python predefined ariable that is set to name f the module in which it is used
# Flask uses the location of the module passed here as a starting point when it needs to load 
# associated resources (like template files)
# for all practical purposes, passing __name__ is almost always going to correctly configure Flask 

# bottom import is a workaround to circular imoprts, a common problem w Flask apps 
from app import routes
