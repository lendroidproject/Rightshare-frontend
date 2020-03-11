import urllib
import json
from flask import Flask, render_template, request, jsonify, redirect
from google.appengine.api import urlfetch
from google.appengine.api import mail
from google.appengine.api import app_identity

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
@app.route('/')
def landing():
    """ Render the Landing page."""
    return 'Hello World Dot', 200
    # return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
