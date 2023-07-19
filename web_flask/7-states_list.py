#!/usr/bin/python3
""" script starts flask web application"""
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ state list """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    return render_template('states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown routine"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
