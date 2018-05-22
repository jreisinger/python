from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/<thingy>/<place>')
def echo(thingy, place):
    return render_template('flask3.html', thingy=thingy, place=place)

# http://localhost:9999/echo2?thingy=bla&place=ble
@app.route('/echo2')
def echo2():
    thingy = request.args.get('thingy')
    place  = request.args.get('place')
    return render_template('flask3.html', thingy=thingy, place=place)

# http://localhost:9999/echo3?thingy=bla&place=ble
@app.route('/echo3')
def echo3():
    # save some typing if there are a lot of arguments
    kwargs = {}
    kwargs['thingy'] = request.args.get('thingy')
    kwargs['place']  = request.args.get('place')
    return render_template('flask3.html', **kwargs)

app.run(port=9999, debug=True)
