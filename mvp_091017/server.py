# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, redirect, request, flash, session, url_for
# from flask_debugtoolbar import DebugToolbarExtension 
# from flask_sqlalchemy import SQLAlchemy # ORM for PostgreSQL database
# import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials as SAC
import gspread
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

# GOOGLE_API_KEY = os.environ['google_api_key'] # source google api key from os environment
GOOGLE_API_KEY = 'AIzaSyBO9CwLQzVNB_dZUUEcsHHFKBkfoqOi8PQ'
app = Flask(__name__) # create instance of Flask app
app.secret_key = 'SECRET_KEY'
app.config['SECRET_KEY']
"""
@app.route('/')
def index():
    # Landing.
    return render_template('index.html')
"""

@app.route('/', methods=['GET'])
def index():
    return '<head><title>VotePledge.US</title><head>'\
           +'<body><h3>Welcome to VotePledge.US</h3><br>'\
            +'<a href="/about">Learn More</a><br><br>'\
            +'<a href="/enterinfo">Get Started</a></body>'
# Below is a Flask App framework I envision for this site.

@app.route('/about', methods=['GET'])
def about():
    return '<h3>VotePledge is aiming to increase voter awareness and commitment. Please Join us.<h3><br>'\
           +'<form action="/enterinfo"><input type="submit" value="Get Started"></form>'
    
@app.route('/enterinfo', methods=['GET', 'POST']) # Interface for when user clicks 'Get Started'
def enterinfo():
    if request.method == 'POST':
        addr = request.form['zipcode'] # gets user's zipcode from '/enterinfo'
        raw_email = request.form['email'] # gets user's name from '/enterinfo'
        try:
            email = validate_email(raw_email)['email']
            API_build = build('civicinfo','v2',developerKey=GOOGLE_API_KEY).representatives()
            API_call = API_build.representativeInfoByAddress(levels='country', roles='legislatorLowerBody',
                                                             address=addr).execute()
            rep=API_call['officials'][0]['name']
            party=API_call['officials'][0]['party'] # different template will render depending on party
            pic = API_call['officials'][0]['photoUrl']
            session['rep'] = rep
            session['party'] = party
            session['email'] = email
            session['pic'] = pic
            return redirect(url_for('repinfo'))
        except EmailNotValidError:
            zipcode_error = ''
            email_error = 'Please enter valid email address to proceed'
            #return render_template('enterinfo2.html', email_error = email_error, zipcode_error = zipcode_error)
        except KeyError:
            email_error = ''
            zipcode_error = 'More than one representative found. Please enter a more specific location.'
            #return render_template('enterinfo2.html', email_error = email_error, zipcode_error = zipcode_error)
        except HttpError:
            email_error = ''
            zipcode_error = 'Could not find information for this location. Check location entered correctly.'
            #return render_template('enterinfo2.html', email_error = email_error, zipcode_error = zipcode_error)
    else:
        email_error = ''
        zipcode_error = ''
        addr = ''
        raw_email = ''
        # template will contain fields for a user's name and zipcode
    return render_template('enterinfo2.html', email_error = email_error, zipcode_error = zipcode_error,
                           zip_value = addr, email_value=raw_email)

@app.route('/repinfo', methods=['GET', 'POST'])
def repinfo():
    party = session['party']
    rep = session['rep']
    pic = session['pic']
    if party == 'Republican':
        return render_template('repinfoGOP.html', rep=rep, pic=pic) # name will be submitted to next page
    elif party == 'Democratic':
        return render_template('repinfoDEM.html', rep=rep, pic=pic)
    else:
        return r'<a href="/enterinfo">First enter your info here</a>'

@app.route('/pledge', methods=['GET', 'POST'])
def pledge():
    rep = request.form['rep']
    #if request.method == 'POST':
        # send submitted data to backend
        # not sure we have that part fully figured out yet
        #redirect(url_for(index))
    return render_template('pledge2.html', rep=rep)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        scope = ['https://spreadsheets.google.com/feeds']
        creds = SAC.from_json_keyfile_name('client_secret.json',scope)
        client = gspread.authorize(creds)
        sheet = client.open('VotePledgeUSData').sheet1
        name = request.form['name']
        rep = session['rep']
        email = session['email']
        message = request.form['message']
        date_time = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S')
        sheet.append_row([name, rep, message, date_time, email])
        return '<h3>Your pledge has been saved. Thanks!</h3>'
    else:
        return 'Error'
#5
if __name__ == "__main__":
    #app.debug = True
    #DebugToolbarExtension(app) # creates toolbar extension
    app.run(debug=True)
