#!/usr/bin/python3
"""
Flask route that returns a list of all State objects
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
