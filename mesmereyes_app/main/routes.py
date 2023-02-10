
from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy import func
from mesmereyes_app.models import InterActivity
from mesmereyes_app.extensions import app, db


main = Blueprint('main', __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    sample_interactivities = InterActivity.query.order_by(func.random()).limit(3).all()
    return render_template('home.html', sample_interactivities=sample_interactivities)


@main.route('/interactivities', methods=['GET', 'POST'])
def interactivities():
    all_interactivities = InterActivity.query.all()
    return render_template('interactivities.html', all_interactivities=all_interactivities)

