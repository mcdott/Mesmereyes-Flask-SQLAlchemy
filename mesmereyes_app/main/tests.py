import os
import unittest
import app

from datetime import date
from mesmereyes_app.extensions import app, db, bcrypt
from mesmereyes_app.models import Doodle, Playlist, User

"""
Run these tests with the command:
python -m unittest mesmereyes_app.main.tests
"""

#################################################
# Setup
#################################################

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password,
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_doodles():
    d1 = Doodle(title='Doodle 1', url='https://www.google.com', cc_attribution='google.com')
    db.session.add(d1)

    d2 = Doodle(title='Doodle 2', url='https://www.google.com', cc_attribution='google.com')
    db.session.add(d2)
    db.session.commit()

def create_user():
    # Creates a user with username 'me1' and password of 'password'
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################

class MainTests(unittest.TestCase):
 
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
    def test_homepage_logged_out(self):
        """Test that the doodles show up on the homepage."""
        # Set up
        create_doodles()
        create_user()

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Doodle 1', response_text)
        self.assertIn('Doodle 2', response_text)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)
        
        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('add doodle', response_text)
        self.assertNotIn('my playlists', response_text)
        self.assertNotIn('add playlist', response_text)
        self.assertNotIn('me1', response_text)
        self.assertNotIn('Log Out', response_text)

    def test_homepage_logged_in(self):
        """Test that the books show up on the homepage."""
        # Set up
        create_doodles()
        create_user()
        login(self.app, 'me1', 'password')

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('add doodle', response_text)
        self.assertIn('my playlists', response_text)
        self.assertIn('add playlist', response_text)
        self.assertIn('me1', response_text)
        self.assertIn('Log Out', response_text)
   

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)


    def test_doodles_logged_out(self):
        """Test that the doodles show up on the doodles page."""
        # Set up
        create_doodles()
        create_user()

        # Make a GET request
        response = self.app.get('/doodles', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Doodle 1', response_text)
        self.assertIn('Doodle 2', response_text)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)
        
        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('add doodle', response_text)
        self.assertNotIn('my playlists', response_text)
        self.assertNotIn('add playlist', response_text)
        self.assertNotIn('me1', response_text)
        self.assertNotIn('Log Out', response_text)

    def test_new_doodle(self):
        """Test that a doodle can be added."""
        # Use helper functions to create a user and log in
        create_user()
        login(self.app, 'me1', 'password')

        # Make a POST request with data
        response = self.app.post('/doodles/new', data=dict(
            title='Doodle 3',
            url='https://www.google.com',
            cc_attribution='google.com'
        ), follow_redirects=True)

        # Check that doodle was added to database
        doodle = Doodle.query.filter_by(title='Doodle 3').first()
        self.assertIsNotNone(doodle)
        self.assertEqual(doodle.title, 'Doodle 3')

# @main.route('/doodle/<int:doodle_id>')
# def doodle(doodle_id):
#     doodle = Doodle.query.get(doodle_id)
#     return render_template('doodle_details.html', doodle=doodle)

# @main.route('/playlists', methods=['GET', 'POST'])
# @login_required
# def playlists():
#     user_playlists = Playlist.query.filter_by(user=current_user).all()
#     return render_template('playlists.html', user_playlists=user_playlists)

# @main.route('/new_playlist', methods=['GET', 'POST'])
# @login_required
# def new_playlist():
#     form = PlaylistForm()

#     # if form was submitted and contained no errors
#     if form.validate_on_submit(): 
#         new_playlist = Playlist(
#             name=request.form['name'],
#             user=current_user
#             )
#         db.session.add(new_playlist)
#         db.session.commit()
#         flash('Playlist added successfully!')
#         return redirect(url_for('main.playlists'))
#     return render_template('new_playlist.html', form=form)


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


# @main.route('/playlist/<int:playlist_id>')
# def playlist(playlist_id):
#     playlist = Playlist.query.get(playlist_id)
#     return render_template('playlist_details.html', playlist=playlist)