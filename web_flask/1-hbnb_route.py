#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """This method is to display a welcome message from the
    page that is hosted"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    """This is a function to display the school name when
    sepcifying the route /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
