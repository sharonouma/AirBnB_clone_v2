#!/usr/bin/python3
"""Starts a Flask web application to display states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """Display a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>')
def state_cities(state_id):
    """Display cities for a specific state"""
    for state in storage.all(State).values():
        if state.id == state_id:
            cities = sorted(state.cities, key=lambda x: x.name)
            return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
