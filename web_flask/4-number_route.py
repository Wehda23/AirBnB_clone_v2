#!/usr/bin/python3
"""
File contains the script to start a flask application
"""
from flask import Flask


# Define application
app = Flask(__name__)


# Define route for the root url "/"
@app.route("/", strict_slashes=False)
def hello_hbnb() -> str:
    """Displays A text message"""
    return "Hello HBNB!"


# Define route for the root url "/"
@app.route("/hbnb", strict_slashes=False)
def hbnb() -> str:
    """Displays A text message"""
    return "HBNB"


# Define route for the root url "/"
@app.route("/c/<text>", strict_slashes=False)
def c_hbnb(text: str) -> str:
    """Displays A text message"""
    return "C {}".format(text.replace("_", " "))


# Define route for the root url "/"
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_hbnb(text: str = "is cool") -> str:
    """Displays A text message"""
    return "Python {}".format(text.replace("_", " "))


# Define route for the root url "/"
@app.route("/number/<int:n>", strict_slashes=False)
def number_hbnb(n: int) -> str:
    """Displays A n message"""
    return "{} is a number".format(n)


# Main
if __name__ == "__main__":
    # Start Flask Server
    app.run(host="0.0.0.0", port=5000)
