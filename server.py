from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension 
from flask_sqlalchemy import SQLAlchemy # ORM for PostgreSQL database
import os

GOOGLE_API_KEY = os.environ['google_api_key'] # source google api key from os environment

app = Flask(__name__) # create instance of Flask app
app.secret_key = 'SECRET_KEY'
app.config['SECRET_KEY']

@app.route('/')
def index():
    """ Landing. """
    return render_template('index.html')





if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app) # creates toolbar extension
    app.run(port=5000, host='0.0.0.0')