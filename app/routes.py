from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
#from flask_login import current_user, login_user, logout_user, login_required
from app import app, db

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])

def index():

    return render_template('index.html', title='Teacher Home')
