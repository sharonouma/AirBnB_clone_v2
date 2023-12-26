#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    "returns a string"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "returns a string"
    return "HBNB"


if __name__ == '__main__':
    app.run()
