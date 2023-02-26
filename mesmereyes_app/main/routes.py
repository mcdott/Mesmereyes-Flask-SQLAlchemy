
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import func
from mesmereyes_app.main.forms import DoodleForm, PlaylistForm, AddDoodleToPlaylistForm
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


# @main.route('/doodles', methods=['GET', 'POST'])
# def doodles():
#     all_doodles = Doodle.query.all()
#     return render_template('doodles.html', all_doodles=all_doodles)

@main.route('/doodles', methods=['GET', 'POST'])
def doodles():
    all_doodles = Doodle.query.all()
    user_playlists = Playlist.query.filter_by(user=current_user).all()

    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        doodle_id = request.form['doodle_id']
        playlist = Playlist.query.get(playlist_id)
        doodle = Doodle.query.get(doodle_id)
        playlist.doodles.append(doodle)
        db.session.commit()
        flash(f'Doodle "{doodle.title}" added to playlist "{playlist.name}"!')

    return render_template('doodles.html', all_doodles=all_doodles, user_playlists=user_playlists)

@main.route('/new_doodle', methods=['GET', 'POST'])
@login_required
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
@login_required
def playlists():
    user_playlists = Playlist.query.filter_by(user=current_user).all()
    return render_template('playlists.html', user_playlists=user_playlists)

@main.route('/new_playlist', methods=['GET', 'POST'])
@login_required
def new_playlist():
    form = PlaylistForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_playlist = Playlist(
            name=request.form['name'],
            user=current_user
            )
        db.session.add(new_playlist)
        db.session.commit()
        flash('Playlist added successfully!')
        return redirect(url_for('main.playlists'))
    return render_template('new_playlist.html', form=form)


# @main.route('/add_doodle_to_playlist/<int:doodle_id>', methods=['GET', 'POST'])
# def add_doodle_to_playlist(doodle_id):
#     doodle = Doodle.query.get(doodle_id)
#     form = AddDoodleToPlaylistForm()
#     form.playlist_id.choices = [(p.id, p.name) for p in Playlist.query.filter_by(user=current_user).all()]
   

#     if form.validate_on_submit():
#         playlist = Playlist.query.get(form.playlist_id.data)
#         playlist.doodles.append(doodle)
#         db.session.commit()
#         flash(f'Doodle "{doodle.title}" added to playlist "{playlist.name}"!')
#         return redirect(url_for('main.playlists'))

#     return render_template('add_doodle_to_playlist.html', doodle=doodle, form=form)


@main.route('/playlist/<int:playlist_id>')
def playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    return render_template('playlist_details.html', playlist=playlist)

@main.route('/delete_playlist/<int:playlist_id>', methods=['POST'])
@login_required
def delete_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if playlist.user == current_user:
        db.session.delete(playlist)
        db.session.commit()
        flash(f'Playlist "{playlist.name}" deleted!')
    else:
        flash('You do not have permission to delete this playlist.')
    return redirect(url_for('main.playlists'))

@main.route('/delete_doodle_from_playlist/<int:playlist_id>/<int:doodle_id>', methods=['POST'])
@login_required
def delete_doodle_from_playlist(playlist_id, doodle_id):
    playlist = Playlist.query.get(playlist_id)
    doodle = Doodle.query.get(doodle_id)
    if doodle in playlist.doodles:
        playlist.doodles.remove(doodle)
        db.session.commit()
        flash(f'Doodle "{doodle.title}" removed from playlist "{playlist.name}"!')
    else:
        flash(f'Doodle "{doodle.title}" is not in playlist "{playlist.name}".')
    return redirect(url_for('main.playlist', playlist_id=playlist_id))


