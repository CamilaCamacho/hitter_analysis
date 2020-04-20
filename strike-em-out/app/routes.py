"""
Home Page Route
Routes are the different URLs that an application implements 
Handlers for application routes are written as Python functions called view functions
View functions are mapped to one or more UEL so that Flask knows what logic to execute when a client requests a given URL
"""
from app import app

# decorators modify the function that follows it
# commonly used to register functions as callbacks for certain events 
# here cerates an association between the URL given as an argument and the function
# meaning: when web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response 
@app.route('/')
@app.route('/index')
# view function that returns greeting as string
def index():
    return "Hello, World!"


