#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Replacing underscore symbols with soaces and returing text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """replacing underscore symbols with spaces and returing text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
