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