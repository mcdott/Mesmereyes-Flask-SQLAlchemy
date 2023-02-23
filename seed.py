from mesmereyes_app.models import Doodle, Level
from mesmereyes_app.extensions import db

# !!! NOTE: In order to seed the database you need to comment out the 'Authentication' 
# section in mesmereyes_app/extensions.py or else you will get an error (circular import)
# when you run python3 seed.py

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
    {
        "title": "Black & white tiles",
        "url": "https://openprocessing.org/sketch/1802452/embed/",
        "cc_attribution": "Black & white tiles by Prakhar Adityahttp://openprocessing.org/sketch/1802452License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.HIGH,
    },
    {
        "title": "Interactive Blob",
        "url": "https://openprocessing.org/sketch/1555443/embed/",
        "cc_attribution": "“Interactive Blob” by Juhani Halkomäkihttp://openprocessing.org/sketch/1555443License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.HIGH,
    },
    {
        "title": "Descendance 6",
        "url": "https://openprocessing.org/sketch/1744394/embed/",
        "cc_attribution": "“Descendance 6 [Sound Sequencer]” by Vamosshttp://openprocessing.org/sketch/1744394License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.LOW
    },
    {
        "title": "Wandering Particles ",
        "url": "https://openprocessing.org/sketch/880007/embed/",
        "cc_attribution": "“Wandering (trailing)Particles” by porthttp://openprocessing.org/sketch/880007License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.HIGH,  
        },
    {
        "title": "0133909",
        "url": "https://openprocessing.org/sketch/972554/embed/",
        "cc_attribution": "“0133909” by Luis Ruizhttp://openprocessing.org/sketch/972554License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.MEDIUM,
    },
    {
        "title": "The Blue Moon",
        "url": "https://openprocessing.org/sketch/1300372/embed/",
        "cc_attribution": "“The Blue Moon - Pixies Involved” by Eleciahttp://openprocessing.org/sketch/1300372License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.HIGH,  
        },
    {
        "title": "drip",
        "url": "https://openprocessing.org/sketch/1247449/embed/",
        "cc_attribution": "“drip” by Aaron Reuland (a_ soluble_fish)http://openprocessing.org/sketch/1247449License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.LOW
    },
    {
        "title": "200417",
        "url": "https://openprocessing.org/sketch/875086/embed/",
        "cc_attribution": "“200417” by Sayamahttp://openprocessing.org/sketch/875086License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.HIGH,
    }
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
