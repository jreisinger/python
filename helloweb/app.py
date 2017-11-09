from flask import Flask
from flask import render_template
from flask import request # for getting user input

app = Flask(__name__)

@app.route("/")
def index():
    return "try '/hello?name=joe' or '/hello_form'"

@app.route("/hello")
def hello():
    name = request.args.get('name', 'Nobody')
    greeting = "Hello, {}".format(name)
    return render_template("index.html", greeting=greeting)

@app.route("/hello_form", methods=['POST', 'GET'])
def hello_form():
    greeting = "Hello world"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = "{0!s}, {1!s}".format(name, greet)
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()
