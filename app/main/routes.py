from flask import render_template, url_for, redirect
from . import main

@main.route('/home')
def home():
    user = {
        'username': None#'luis.gurrola'
    }

    return render_template('main/home.html', user=user)