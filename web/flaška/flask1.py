#!/usr/bin/env python3

## Initialization

# Create application instance that will handle all requests from clients.
# Requtests are passed by the web server using WSGI ("wiz-ghee") protocol.

# Defaults for static_folder and static_url_path is 'static'.
from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')

## Routes and view functions

# Define what code to run for each URL. These mappings of URLs to Python
# functions are called routes. Functions like home() are called view functions.

# Decorators are used to register functions as handler functions to be invoked
# when certain events occur.
@app.route('/')

def home():
    return app.send_static_file('index.html')

# dynamic route
@app.route('/echo/<string:thingy>')
def echo(thingy):
    return thingy

app.run(port=9999, debug=True)

## To run this app:
#
# export FLASK_APP=flask1.py
# flask run
