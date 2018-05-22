#!/usr/bin/env python3

from flask import Flask

# defaults for static_folder and static_url_path is 'static'
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thingy>')
def echo(thingy):
    return thingy

app.run(port=9999, debug=True)
