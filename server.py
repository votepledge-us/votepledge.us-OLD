from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension 
from flask_sqlalchemy import SQLAlchemy # ORM for PostgreSQL database
import os
#from googleapiclient.civicinfo.representatives import representativesByAddress

GOOGLE_API_KEY = os.environ['google_api_key'] # source google api key from os environment

app = Flask(__name__) # create instance of Flask app
app.secret_key = 'SECRET_KEY'
app.config['SECRET_KEY']

@app.route('/')
def index():
    """ Landing. """
    return render_template('index.html')

# Below is a Flask App framework I envision for this site.
# Template files referenced don't yet exist.

"""
@app.route('/enterinfo') # Interface for when user clicks 'Get Started'
def enterinfo():
    # template will contain fields for a user's name and zipcode
    render_template('enterinfo.html')

@app.route('/repinfo')
def repinfo():
    addr = request.form['zipcode'] # gets user's zipcode from '/enterinfo'
    name = request.form['name'] # gets user's name from '/enterinfo'
    API_call = representativeInfoByAddress(levels='country', roles='legislatorLowerBody',
                                           address=addr)
    rep=API_call['officials'][0]['name']
    party=API_call['officials'][0]['party'] # different template will render depending on party
    if party == 'Republican':
        render_template('repinfoGOP.html', name=name, rep=rep) # name will be submitted to next page
    elif party == 'Democratic':
        render_template('repinfoDEM.html', name=name, rep=rep)

@app.route('/pledge')
def pledge():
    name = request.args.get('name', None)
    rep = request.args.get('rep', None)
    if request.method == 'POST':
        # send submitted data to backend
    render_template('pledge.html', name=name, rep=rep)
""" 

if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app) # creates toolbar extension
    app.run(port=5000, host='0.0.0.0')
