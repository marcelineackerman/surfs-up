from flask import Flask

#Create a new flask app instance

app = Flask(__name__)

@app.route('/')

def hello_world():

    return 'Hello world'