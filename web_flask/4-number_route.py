#!/usr/bin/python3
"""Mininmalist web application with flask"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return 'hello HBNB' to browser"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb_route():
    """Return 'HBNB' to browser"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """concatenate the value passed through url\
       and display on browser
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Adding default value to url variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display n in the browser if is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
