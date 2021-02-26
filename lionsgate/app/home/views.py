from flask import abort, render_template, flash, redirect, url_for, current_app
from . import home

@home.route('/')
def homepage():
    return render_template('index.html')
