
from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy import func
from mesmereyes_app.main.forms import InterActivityForm
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

@main.route('/new_interactivity', methods=['GET', 'POST'])
def new_interactivity():
    form = InterActivityForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_interactivity = InterActivity(
            title=request.form['title'],
            url=request.form['url'],
            cc_attribution=request.form['cc_attribution'],
            visual_complexity=request.form['visual_complexity'],
            visual_contrast=request.form['visual_contrast']
            )
        db.session.add(new_interactivity)
        db.session.commit()
        flash('Interactivity added successfully.')
        return redirect(url_for('main.interactivities'))
    return render_template('new_interactivity.html', form=form)