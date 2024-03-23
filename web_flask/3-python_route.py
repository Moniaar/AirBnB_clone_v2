#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
	"""This method is to display a welcome message from the page that is hosted"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display():
	"""This is a function to display the school name when sepcifying the route /hbnb"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
	"""A method to display “C ” followed by the value of the text variable"""
	text = text.replace("_", " ")
	return 'C' + text.replace('_', ' ')
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_C(text='is cool'):
	"""A method to display “python” followed by the value of the text variable"""
	text = text.replace("_", " ")
	return 'Python' + text.replace('_', ' ')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

