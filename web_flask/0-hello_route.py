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


# Main
if __name__ == "__main__":
    # Start Flask Server
    app.run(host="0.0.0.0", port=5000)
