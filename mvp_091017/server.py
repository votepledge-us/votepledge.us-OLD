from flask import Flask, jsonify, render_template, redirect, request, flash, session, url_for
# from flask_debugtoolbar import DebugToolbarExtension 
# from flask_sqlalchemy import SQLAlchemy # ORM for PostgreSQL database
# import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials as SAC
import gspread
from datetime import datetime

# GOOGLE_API_KEY = os.environ['google_api_key'] # source google api key from os environment
GOOGLE_API_KEY = 'AIzaSyBO9CwLQzVNB_dZUUEcsHHFKBkfoqOi8PQ'
app = Flask(__name__) # create instance of Flask app
#app.secret_key = 'SECRET_KEY'
#app.config['SECRET_KEY']
"""
@app.route('/')
def index():
    # Landing.
    return render_template('index.html')
"""

@app.route('/')
def index():
    return '<h3>INDEX</h3>'
# Below is a Flask App framework I envision for this site.

@app.route('/enterinfo', methods=['GET', 'POST']) # Interface for when user clicks 'Get Started'
def enterinfo():
    # template will contain fields for a user's name and zipcode
    return render_template('enterinfo.html')

@app.route('/repinfo', methods=['GET', 'POST'])
def repinfo():
    if request.method == 'POST':
        addr = request.form['zipcode'] # gets user's zipcode from '/enterinfo'
        name = request.form['name'] # gets user's name from '/enterinfo'
        API_build = build('civicinfo','v2',developerKey=GOOGLE_API_KEY).representatives()
        API_call = API_build.representativeInfoByAddress(levels='country', roles='legislatorLowerBody',
                                                         address=addr).execute()
        rep=API_call['officials'][0]['name']
        party=API_call['officials'][0]['party'] # different template will render depending on party
        if party == 'Republican':
            return render_template('repinfoGOP.html', name=name, rep=rep) # name will be submitted to next page
        elif party == 'Democratic':
            return render_template('repinfoDEM.html', name=name, rep=rep)
    else:
        return r'<a href="/enterinfo">First enter your info here</a>'

@app.route('/pledge', methods=['GET', 'POST'])
def pledge():
    name = request.form['name']
    rep = request.form['rep']
    #if request.method == 'POST':
        # send submitted data to backend
        # not sure we have that part fully figured out yet
        #redirect(url_for(index))
    return render_template('pledge.html', name=name, rep=rep)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        scope = ['https://spreadsheets.google.com/feeds']
        creds = SAC.from_json_keyfile_name('client_secret.json',scope)
        client = gspread.authorize(creds)
        sheet = client.open('VotePledgeUSData').sheet1
        name = request.form['name']
        rep = request.form['rep']
        message = request.form['message']
        date_time = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S')
        sheet.append_row([name, rep, message, date_time])
        return '<h3>Your pledge has been saved. Thanks!</h3>'
    else:
        return 'Error'
#5
if __name__ == "__main__":
    #app.debug = True
    #DebugToolbarExtension(app) # creates toolbar extension
    app.run(debug=True)
