from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thingy>')
def echo(thingy):
    return render_template('flask2.html', thingy=thingy)

app.run(port=9999, debug=True)
