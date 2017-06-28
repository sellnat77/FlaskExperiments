import os
import config as cfg
import logger as log
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

##################
# Gloabal Vars
##################

ENDPOINTS = ['index', 'youtubedemo', 'coolRender']

##################
# Gloabal Vars
##################


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', ENDPOINTS=ENDPOINTS)

@app.route('/youtubedemo', methods=['GET','POST'])
def youtubedemo():
    return render_template('youtubedemo.html', ENDPOINTS=ENDPOINTS)

@app.route('/coolRender', methods=['GET','POST'])
def coolRender():
    #log.log(ytLink, cfg.ConfigVars['LogLevel'])
    return render_template('coolRender.html', ENDPOINTS=ENDPOINTS)

@app.route('/particles', methods=['GET','POST'])
def particles():
    #log.log(ytLink, cfg.ConfigVars['LogLevel'])
    return render_template('particles.html', ENDPOINTS=ENDPOINTS, DaBoi='Russell Crowe')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
