from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    # Flask uses *contexts* to temporarily make certain objects globally
    # accessible. `request` is used as it were a global variable.
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
