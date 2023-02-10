from mesmereyes_app.models import InterActivity, Level
from mesmereyes_app.extensions import db

# Connect to the database
db.create_all()

# Define your data
data = [
    {
        'title': 'Interactivity 1',
        'url': 'https://www.example.com/interactivity1',
        'cc_attribution': 'Attribution 1',
        'visual_complexity': Level.LOW,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Interactivity 2',
        'url': 'https://www.example.com/interactivity2',
        'cc_attribution': 'Attribution 2',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.LOW
    },
    {
        'title': 'Interactivity 3',
        'url': 'https://www.example.com/interactivity3',
        'cc_attribution': 'Attribution 3',
        'visual_complexity': Level.LOW,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Interactivity 4',
        'url': 'https://www.example.com/interactivity4',
        'cc_attribution': 'Attribution 4',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.LOW
    },
]

# Insert the data into the database
for item in data:
    inter_activity = InterActivity(
        title=item['title'],
        url=item['url'],
        cc_attribution=item['cc_attribution'],
        visual_complexity=item['visual_complexity'],
        visual_contrast=item['visual_contrast']
    )
    db.session.add(inter_activity)

# Commit the changes
db.session.commit()
