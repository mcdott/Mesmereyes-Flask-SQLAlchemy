
from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy import func
from mesmereyes_app.main.forms import DoodleForm, PlaylistForm
from mesmereyes_app.models import Doodle, Playlist
from mesmereyes_app.extensions import app, db


main = Blueprint('main', __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    sample_doodles = Doodle.query.order_by(func.random()).limit(3).all()
    return render_template('home.html', sample_doodles=sample_doodles)


@main.route('/doodles', methods=['GET', 'POST'])
def doodles():
    all_doodles = Doodle.query.all()
    return render_template('doodles.html', all_doodles=all_doodles)

@main.route('/new_doodle', methods=['GET', 'POST'])
def new_doodle():
    form = DoodleForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_doodle = Doodle(
            title=request.form['title'],
            url=request.form['url'],
            cc_attribution=request.form['cc_attribution'],
            visual_complexity=request.form['visual_complexity'],
            visual_contrast=request.form['visual_contrast']
            )
        db.session.add(new_doodle)
        db.session.commit()
        flash('Doodle added successfully!')
        return redirect(url_for('main.doodles'))
    return render_template('new_doodle.html', form=form)

@main.route('/doodle/<int:doodle_id>')
def doodle(doodle_id):
    doodle = Doodle.query.get(doodle_id)
    return render_template('doodle_details.html', doodle=doodle)

@main.route('/playlists', methods=['GET', 'POST'])
def playlists():
    all_playlists = Playlist.query.all()
    return render_template('playlists.html', all_playlists=all_playlists)

@main.route('/new_playlist', methods=['GET', 'POST'])
def new_playlist():
    form = PlaylistForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_playlist = Playlist(
            name=request.form['name']
            )
        db.session.add(new_playlist)
        db.session.commit()
        flash('Playlist added successfully!')
        return redirect(url_for('main.playlists'))
    return render_template('new_playlist.html', form=form)

