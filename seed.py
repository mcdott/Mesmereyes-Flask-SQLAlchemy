from mesmereyes_app.models import Doodle, Level
from mesmereyes_app.extensions import db

# Connect to the database
db.create_all()

# Define your data
data = [
    {
        'title': 'Particle chunk',
        'url': 'http://openprocessing.org/sketch/1619381/embed/',
        'cc_attribution': ' “Particle chunk” by Juhani Halkomäkihttp://openprocessing.org/sketch/1619381License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.MEDIUM
    },
    {
        'title': 'Blob Soup',
        'url': 'http://openprocessing.org/sketch/1620516/embed/',
        'cc_attribution': 'Attribution 2',
        'visual_complexity': Level.HIGH,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Particles',
        'url': 'https://openprocessing.org/sketch/1786759/embed/',
        'cc_attribution': '“Particles” by Naoki Tsutaehttp://openprocessing.org/sketch/1786759License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Frozen Brush',
        'url': 'https://openprocessing.org/sketch/413567/embed/',
        'cc_attribution': '“Frozen brush” by Jason Labbehttp://openprocessing.org/sketch/413567License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0',
        'visual_complexity': Level.LOW,
        'visual_contrast': Level.HIGH
    },
]

# Insert the data into the database
for item in data:
    doodle = Doodle(
        title=item['title'],
        url=item['url'],
        cc_attribution=item['cc_attribution'],
        visual_complexity=item['visual_complexity'],
        visual_contrast=item['visual_contrast']
    )
    db.session.add(doodle)

# Commit the changes
db.session.commit()
