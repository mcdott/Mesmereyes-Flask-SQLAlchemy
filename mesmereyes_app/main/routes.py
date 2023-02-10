from flask import Blueprint, request, render_template, redirect, url_for, flash
from mesmereyes_app.models import InterActivity

from mesmereyes_app.extensions import app, db

main = Blueprint('main', __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_interactivities = InterActivity.query.all()
    print(all_interactivities)
    return render_template('home.html', all_interactivities=all_interactivities)


# @main.route('/')
# def homepage():
#     return render_template('home.html')


