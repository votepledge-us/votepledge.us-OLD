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
from healthcaredict import healthcaredict

# GOOGLE_API_KEY = os.environ['google_api_key'] # source google api key from os environment
GOOGLE_API_KEY = ###
app = Flask(__name__) # create instance of Flask app
app.secret_key = 'SECRET_KEY'
app.config['SECRET_KEY']
"""
@app.route('/')
def index():
    # Landing.
    return render_template('index.html')
"""
#4
transitions0 = {0: {'indexcss': '',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                1: {'indexcss': 'class="animated slideInLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideOutRight"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                2: {'indexcss': 'class="animated slideInLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideOutRight"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                3: {'indexcss': 'class="animated slideInLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideOutRight"',
                    'thankscss': 'style="display:none;"'},
                4: {'indexcss': 'class="animated slideInLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideOutRight"'}}
transitions1 = {0: {'indexcss': 'class="animated slideOutLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideInRight"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                1: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': '',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                2: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideInLeft"',
                    'repinfocss': 'class="animated slideOutRight"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                3: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideInLeft"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideOutRight"',
                    'thankscss': 'style="display:none;"'},
                4: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideInLeft"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideOutRight"'}}
transitions2 = {0: {'indexcss': 'class="animated slideOutLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideInRight"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                1: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideOutLeft"',
                    'repinfocss': 'class="animated slideInRight"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                2: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': '',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'style="display:none;"'},
                3: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideInLeft"',
                    'pledgecss': 'class="animated slideOutRight"',
                    'thankscss': 'style="display:none;"'},
                4: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideInLeft"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideOutRight"'}}
transitions3 = {0: {'indexcss': 'class="animated slideOutLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideInRight"',
                    'thankscss': 'style="display:none;"'},
                1: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideOutLeft"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideInRight"',
                    'thankscss': 'style="display:none;"'},
                2: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideOutLeft"',
                    'pledgecss': 'class="animated slideInRight"',
                    'thankscss': 'style="display:none;"'},
                3: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': '',
                    'thankscss': 'style="display:none;"'},
                4: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideInLeft"',
                    'thankscss': 'class="animated slideOutRight"'}}
transitions4 = {0: {'indexcss': 'class="animated slideOutLeft"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideInRight"'},
                1: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'class="animated slideOutLeft"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideInRight"'},
                2: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'class="animated slideOutLeft"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': 'class="animated slideInRight"'},
                3: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'class="animated slideOutLeft"',
                    'thankscss': 'class="animated slideInRight"'},
                4: {'indexcss': 'style="display:none;"',
                    'aboutcss': 'style="display:none;"',
                    'enterinfocss': 'style="display:none;"',
                    'repinfocss': 'style="display:none;"',
                    'pledgecss': 'style="display:none;"',
                    'thankscss': ''}}

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, max-age=0, must-revalidate, no-store'
    return response

@app.route('/', methods=['GET'])
def index():
    title = 'VotePledge.us'
    try:
        indexcss = transitions0[session['CurrentPage']]['indexcss']
        aboutcss = transitions0[session['CurrentPage']]['aboutcss']
        enterinfocss = transitions0[session['CurrentPage']]['enterinfocss']
        repinfocss = transitions0[session['CurrentPage']]['repinfocss']
        pledgecss = transitions0[session['CurrentPage']]['pledgecss']
        thankscss = transitions0[session['CurrentPage']]['thankscss']
    except KeyError:
        indexcss = transitions0[0]['indexcss']
        aboutcss = transitions0[0]['aboutcss']
        enterinfocss = transitions0[0]['enterinfocss']
        repinfocss = transitions0[0]['repinfocss']
        pledgecss = transitions0[0]['pledgecss']
        thankscss = transitions0[0]['thankscss']
    session['CurrentPage'] = 0
    return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, enterinfocss=enterinfocss,repinfocss=repinfocss,
                               pledgecss=pledgecss,thankscss=thankscss, title=title)
# Below is a Flask App framework I envision for this site.

@app.route('/about', methods=['GET'])
def about():
    title = 'About Us|VotePledge.us'
    indexcss = 'style="display:none;"'
    aboutcss = ''
    enterinfocss = 'style="display:none;"'
    repinfocss = 'style="display:none;"'
    pledgecss = 'style="display:none;"'
    thankscss = 'style="display:none;"'
    session['CurrentPage'] = 'None'
    return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, enterinfocss=enterinfocss,repinfocss=repinfocss,
                               pledgecss=pledgecss,thankscss=thankscss, title=title)
    
@app.route('/enterinfo', methods=['GET', 'POST']) # Interface for when user clicks 'Get Started'
def enterinfo():
    title = 'Find Rep'
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
    try:
        indexcss = transitions1[session['CurrentPage']]['indexcss']
        aboutcss = transitions1[session['CurrentPage']]['aboutcss']
        enterinfocss = transitions1[session['CurrentPage']]['enterinfocss']
        repinfocss = transitions1[session['CurrentPage']]['repinfocss']
        pledgecss = transitions1[session['CurrentPage']]['pledgecss']
        thankscss = transitions1[session['CurrentPage']]['thankscss']
    except KeyError:
        indexcss = transitions1[1]['indexcss']
        aboutcss = transitions1[1]['aboutcss']
        enterinfocss = transitions1[1]['enterinfocss']
        repinfocss = transitions1[1]['repinfocss']
        pledgecss = transitions1[1]['pledgecss']
        thankscss = transitions1[1]['thankscss']
    session['CurrentPage'] = 1
    return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, email_error = email_error, zipcode_error = zipcode_error,
                           zip_value = addr, email_value=raw_email,repinfocss=repinfocss, title=title,
                           pledgecss=pledgecss,thankscss=thankscss, enterinfocss=enterinfocss)

@app.route('/repinfo', methods=['GET', 'POST'])
def repinfo():
    party = session['party']
    rep = session['rep']
    pic = session['pic']
    title = '{}'.format(rep)
    if healthcaredict[rep] == 1:
        copy = '{} has voted to take away healthcare from millions '.format(rep)
        copy += 'Let them know you will not be voting for them because of this.'
        button = 'I pledge to vote against {}.'.format(rep)
    elif healthcaredict[rep] == 0:
        copy = '{} has voted to preserve the ACA. Send them a message and '.format(rep)
        copy += 'let them know you expect their continued support of healthcare.'
        button = 'Tell {} why you support them.'.format(rep)
    if party != None:
        try:
            indexcss = transitions2[session['CurrentPage']]['indexcss']
            aboutcss = transitions2[session['CurrentPage']]['aboutcss']
            enterinfocss = transitions2[session['CurrentPage']]['enterinfocss']
            repinfocss = transitions2[session['CurrentPage']]['repinfocss']
            pledgecss = transitions2[session['CurrentPage']]['pledgecss']
            thankscss = transitions2[session['CurrentPage']]['thankscss']
        except KeyError:
            indexcss = transitions2[2]['indexcss']
            aboutcss = transitions2[2]['aboutcss']
            enterinfocss = transitions2[2]['enterinfocss']
            repinfocss = transitions2[2]['repinfocss']
            pledgecss = transitions2[2]['pledgecss']
            thankscss = transitions2[2]['thankscss']
        session['CurrentPage'] = 2
        return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, copy=copy,pic=pic,enterinfocss=enterinfocss,repinfocss=repinfocss,
                               pledgecss=pledgecss,thankscss=thankscss, button = button, title=title)
    else:
        return r'<a href="/enterinfo">First enter your info here</a>'

@app.route('/pledge', methods=['GET', 'POST'])
def pledge():
    title = 'Pledge'
    rep = session['rep']
    if healthcaredict[rep] == 1:
        pledgecopy = 'will not be voting {}.'.format(rep)
    elif healthcaredict[rep] == 0:
        pledgecopy = 'support {} thanks to their support of the ACA.'.format(rep)
    try:
        indexcss = transitions3[session['CurrentPage']]['indexcss']
        aboutcss = transitions3[session['CurrentPage']]['aboutcss']
        enterinfocss = transitions3[session['CurrentPage']]['enterinfocss']
        repinfocss = transitions3[session['CurrentPage']]['repinfocss']
        pledgecss = transitions3[session['CurrentPage']]['pledgecss']
        thankscss = transitions3[session['CurrentPage']]['thankscss']
    except KeyError:
        indexcss = transitions3[3]['indexcss']
        aboutcss = transitions3[3]['aboutcss']
        enterinfocss = transitions3[3]['enterinfocss']
        repinfocss = transitions3[3]['repinfocss']
        pledgecss = transitions3[3]['pledgecss']
        thankscss = transitions3[3]['thankscss']
    session['CurrentPage'] = 3
    return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, pledgecopy = pledgecopy,enterinfocss=enterinfocss,repinfocss=repinfocss,
                           pledgecss=pledgecss,thankscss=thankscss, title=title, rep=rep)
#4
@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    title = 'Thanks!'
    if request.method == 'POST':
        scope = ['https://spreadsheets.google.com/feeds']
        creds = SAC.from_json_keyfile_name('client_secret.json',scope)
        client = gspread.authorize(creds)
        sheet = client.open('VotePledgeUSData').sheet1
        name = request.form['name']
        rep = session['rep']
        email = session['email']
        message = request.form['message']
        healthcarevote = healthcaredict[rep]
        date_time = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S')
        sheet.append_row([name, rep, message, date_time, email, healthcarevote])
        try:
            indexcss = transitions4[session['CurrentPage']]['indexcss']
            aboutcss = transitions4[session['CurrentPage']]['aboutcss']
            enterinfocss = transitions4[session['CurrentPage']]['enterinfocss']
            repinfocss = transitions4[session['CurrentPage']]['repinfocss']
            pledgecss = transitions4[session['CurrentPage']]['pledgecss']
            thankscss = transitions4[session['CurrentPage']]['thankscss']
        except KeyError:
            indexcss = transitions4[4]['indexcss']
            aboutcss = transitions4[4]['aboutcss']
            enterinfocss = transitions4[4]['enterinfocss']
            repinfocss = transitions4[4]['repinfocss']
            pledgecss = transitions4[4]['pledgecss']
            thankscss = transitions4[4]['thankscss']
        session['CurrentPage'] = 4
        return render_template('votepledge.html', indexcss=indexcss, aboutcss=aboutcss, enterinfocss=enterinfocss,repinfocss=repinfocss,
                               pledgecss=pledgecss,thankscss=thankscss, title=title)
    else:
        return 'Error'
#5
if __name__ == "__main__":
    #app.debug = True
    #DebugToolbarExtension(app) # creates toolbar extension
    app.run(debug=True)
