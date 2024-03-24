#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """This method is to display a welcome message from
    the page that is hosted"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    """This is a function to display the school name when
    sepcifying the route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """A method to display “C ” followed by the value of
    the text variable"""
    text = text.replace("_", " ")
    return 'C ' + text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text='is cool'):
    """A method to display “python” followed by the value
    of the text variable"""
    text = text.replace("_", " ")
    return 'Python ' + text


@app.route("/number/<int:n>", strict_slashes=False)
def route_numb(n):
    """This is script that starts a Flask web application with numbers"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """This is a function to deploy the jinja template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
