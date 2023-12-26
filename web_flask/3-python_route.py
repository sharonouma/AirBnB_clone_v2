#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """returns a string"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns a string"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """displays a string"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """displays a string"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
