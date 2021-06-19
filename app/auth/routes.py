from flask import render_template
from . import auth

@auth.route('/index')
def index():

    return render_template('index.html')