#!/usr/bin/python3
"""
File that contains a flask api to call all states
"""
from flask import Flask, render_template
from models import storage

# Flask Application
app = Flask(__name__)


# Api
@app.route("/states_list", strict_slashes=False)
def states_view() -> object:
    """
    View that returns states
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
