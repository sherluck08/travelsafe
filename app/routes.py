from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.forms import LocationForm
#from flask_login import current_user, login_user, logout_user, login_required
from app import app, db

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = LocationForm()
    if form.validate_on_submit():
        print("success")
        url = "https://www.pythonprogramming.in/media/wysiwyg/matplotlib/mat-7.png"
        data = [url]
        print(data)

    return render_template('index.html', title='Teacher Home', form=form)
