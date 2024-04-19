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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
