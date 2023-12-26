#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template


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


@app.route("/number/<int:n>")
def number(n):
    """displays n only if it is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def template(n):
    """displays a html page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """displays a html page if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
