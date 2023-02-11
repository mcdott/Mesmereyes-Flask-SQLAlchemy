from sqlalchemy_utils import URLType
from flask_login import UserMixin
from mesmereyes_app.extensions import db
from mesmereyes_app.utils import FormEnum

class Level(FormEnum):
    """Levels of visual complexity and contrast."""
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

playlist_doodles = db.Table('playlist_doodles',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
    db.Column('doodle_id', db.Integer, db.ForeignKey('doodle.id'))
)
class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    doodles = db.relationship('Doodle', secondary=playlist_doodles, back_populates='playlists')

class Doodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    url = db.Column(URLType)
    cc_attribution = db.Column(db.Text)
    visual_complexity = db.Column(db.Enum(Level), default=Level.MEDIUM)
    visual_contrast = db.Column(db.Enum(Level), default=Level.MEDIUM)
    playlists = db.relationship('Playlist', secondary=playlist_doodles, back_populates='doodles')



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    # playlists = db.relationship(
    #     'Playlist', secondary='user_playlist', back_populates='users_who_selected')
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=True)
    playlists = db.relationship(
        'Playlist', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<User: {self.username}>'

user_playlists = db.Table('user_playlist',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'))
)