#!/usr/bin/python3
"""minimal flask application"""

from flask import Flask


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns 'HBNB' string to the browser"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Returns 'Hello HBNB' string to the browser"""
    return "Hello HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Takes variable value from url and process it"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """processing variable for the /python route"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
