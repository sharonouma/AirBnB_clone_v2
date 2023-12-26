#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb')
def hbnb():
    """Display a HTML page like 8-index.html"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    cities = sorted(storage.all("City").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    places = sorted(storage.all("Place").values(), key=lambda x: x.name)
    return render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
