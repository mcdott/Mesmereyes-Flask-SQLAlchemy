from sqlalchemy_utils import URLType
# from flask_login import UserMixin
from mesmereyes_app.extensions import db
from mesmereyes_app.utils import FormEnum

class Level(FormEnum):
    """Levels of visual complexity and contrast."""
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class Doodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    url = db.Column(URLType)
    cc_attribution = db.Column(db.Text)
    visual_complexity = db.Column(db.Enum(Level), default=Level.MEDIUM)
    visual_contrast = db.Column(db.Enum(Level), default=Level.MEDIUM)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

playlist_doodles = db.Table('playlist_doodles',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
    db.Column('doodle_id', db.Integer, db.ForeignKey('doodle.id'))
)