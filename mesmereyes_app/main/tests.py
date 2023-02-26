import os
import unittest
import app

from datetime import date
from mesmereyes_app.extensions import app, db, bcrypt
from mesmereyes_app.models import Doodle, Playlist, User

"""
Run these tests with the command:
python3 -m unittest mesmereyes_app.main.tests
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
    # Creates a user with username 'me1', email 'me1@test.com',
    # and password 'password'
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', email='me1@test.com', password=password_hash)
    db.session.add(user)
    db.session.commit()

def create_playlists():
    p1 = Playlist(name='Playlist 1', user_id=1)
    db.session.add(p1)

    p2 = Playlist(name='Playlist 2', user_id=1)
    db.session.add(p2)
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
        self.assertNotIn('Log Out', response_text)

    def test_homepage_logged_in(self):
        """Test that the doodles show up on the homepage."""
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
        self.assertIn('Log Out', response_text)
   

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)

    def test_doodles_logged_in(self):
        """Test that the doodles show up on the doodles page."""
        # Set up
        create_doodles()
        create_user()
        login(self.app, 'me1', 'password')

        # Make a GET request
        response = self.app.get('/doodles', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('add doodle', response_text)
        self.assertIn('my playlists', response_text)
        self.assertIn('add playlist', response_text)
        self.assertIn('Log Out', response_text)

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)

    def test_new_doodle(self):
        """Test that a doodle can be added."""
        # Use helper functions to create a user and log in
        create_user()
        login(self.app, 'me1', 'password')

        # Make a POST request with data
        response = self.app.post('/new_doodle', data=dict(
            title='New Doodle',
            url='https://www.example.com',
            cc_attribution='example.com',
            visual_complexity='MEDIUM',
            visual_contrast='MEDIUM'
        ), follow_redirects=True)

        # Check that doodle was added to database
        doodle = Doodle.query.filter_by(title='New Doodle').first()
        self.assertIsNotNone(doodle)


    def test_doodle(self):
        """Test that the doodle details page shows up."""
        # Set up
        create_doodles()
        create_user()

        # Make a GET request
        response = self.app.get('/doodle/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Doodle 1', response_text)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)
        
        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('add doodle', response_text)
        self.assertNotIn('my playlists', response_text)
        self.assertNotIn('add playlist', response_text)
        self.assertNotIn('Log Out', response_text)

    def test_playlists_logged_in(self):
        """Test that the playlists page shows up."""
        # Use helper functions to create a user and log in
        create_user()
        login(self.app, 'me1', 'password')
        create_doodles()
        create_playlists()

        # Make a GET request
        response = self.app.get('/playlists', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Playlist 1', response_text)
        self.assertIn('Playlist 2', response_text)
        self.assertIn('Log Out', response_text)
        self.assertIn('add doodle', response_text)
        self.assertIn('my playlists', response_text)
        self.assertIn('add playlist', response_text)
        
        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)

    def test_new_playlist_logged_in(self):
        """Test that a playlist can be added."""
        # Use helper functions to create a user and log in
        create_user()
        login(self.app, 'me1', 'password')

        # Make a POST request with data
        response = self.app.post('/new_playlist', data=dict(
            name='New Playlist',
        ), follow_redirects=True)
        
        # Check that playlist was added to database
        playlist = Playlist.query.filter_by(name='New Playlist').first()
        self.assertIsNotNone(playlist)

    def test_playlist(self):
        """Test that the playlist details page shows up."""
        # Set up
        create_doodles()
        create_user()
        create_playlists()

        # Make a GET request
        response = self.app.get('/playlist/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Playlist 1', response_text)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)
        
        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('add doodle', response_text)
        self.assertNotIn('my playlists', response_text)
        self.assertNotIn('add playlist', response_text)
        self.assertNotIn('Log Out', response_text)

    def test_delete_doodle_from_playlist_logged_in(self):
        """Test that a doodle can be removed from a playlist."""
        # Use helper functions to create a user, log in, create a playlist, and add a doodle to the playlist
        create_user()
        login(self.app, 'me1', 'password')
        create_doodles()
        create_playlists()
        response = self.app.post('/doodles', data=dict(
            playlist_id=1,
            doodle_id=1
        ), follow_redirects=True)

        # Check that the playlist exists and has the doodle
        playlist = Playlist.query.get(1)
        self.assertIsNotNone(playlist)
        doodle = Doodle.query.get(1)
        self.assertIn(doodle, playlist.doodles)

        # Remove the doodle from the playlist
        response = self.app.post('/delete_doodle_from_playlist/1/1', follow_redirects=True)

        # Check that the playlist no longer has the doodle
        playlist = Playlist.query.get(1)
        self.assertNotIn(doodle, playlist.doodles)
