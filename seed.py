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
        'url': "https://openprocessing.org/sketch/1619381/embed/?plusEmbedHash=Nzk4N2JjMDUyNTdiODZhYzlhZTgyNzEyMjAzM2M1NzFjNmY3ZGJhNGM3MWQ0ZTUyYjZkN2U3NjRjNjZiZmMzYTAzMDRlZjhlMzVkODIwNmY1NGM0YzMxYTk0OTg2MjVkZTEwMzBmNmMwYzE5MTdmYWE1OGM2MWRlZDEzNTA3MDRQdUJCSXZVdFlyTDlGM2o2ejk2WUY5QjFldHVhbDVndU9pbUhuUlFIbTVlR2ZEZ0RPdGVLM3RoQWF2RHJGZGpEOU95NEpoYWZnU1NyMUU1by9yTXQ0UT09",
        'cc_attribution': ' “Particle chunk” by Juhani Halkomäkihttp://openprocessing.org/sketch/1619381License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.MEDIUM
    },
    {
        'title': 'Blob Soup',
        'url':  "https://openprocessing.org/sketch/1620516/embed/?plusEmbedHash=ZTJjZjExNGQxYmM1ZjRiYWVmNTQ3YTc1Mzg1MmRiNjI1NTI1ODRhYTNmOGU5M2YwY2FiNWY3OWVmMDM0NmRhNmM5ZjA4NTliYzkwMDM0YzRiZDU0MGRkNjdiMmJmYTM3YjVjNjEzMzQ0NGFlYzQ1MWFiMmIxNmU0ZDMwZDRhMzJGWTdkbVNOanVxeXNpZWlXZUo1THY2SEVnNzUvQWozZEVSUVNTL1RrTy9iSkJBbVVXSXBKZlFQalNqbDhNQ2hWUUR2OFg0bG9XMjFNYTNuTlVydkt2dz09",
        'cc_attribution': 'Attribution 2',
        'visual_complexity': Level.HIGH,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Particles',
        'url': "https://openprocessing.org/sketch/1786759/embed/?plusEmbedHash=MjQ1MjFlYmVjZTQxNmMyM2IyZmY5NzgyMjBlMDQ3OTNmMjNkOGVhZGE3NjE2NzE5MTRmMDYxNmMzMjM0Y2M3OWQxZTkyZTY2NzFlMjBhNzY2MzUwYTllZTNhNjdkNzE1NGUyMTQ1YzkyMzMxYTgwYWRiZTAyZGU0MDRhZmQ3MGI1dDcvNG5LUVBwUmlZd3BmMXJRWHhKcFdoY0J6UmtYckNWY1hXS2hiZEdjWmdCaUZremVJbFdWYTFzd0Q4blpUQ2dwM0FKbDkxQ05USFA1MXFCcnZBQT09",
        'cc_attribution': '“Particles” by Naoki Tsutaehttp://openprocessing.org/sketch/1786759License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0',
        'visual_complexity': Level.MEDIUM,
        'visual_contrast': Level.HIGH
    },
    {
        'title': 'Frozen Brush',
        'url': "https://openprocessing.org/sketch/413567/embed/?plusEmbedHash=ZmQ0ZTU4ZmViNWU0ZGQ5YTQ2MWM4YWU3YzU2Y2FlNDMwZWYyZWYxZDQ3ODJhOWJjOWY0ZjQ0MWJjMzJjODY1YTdhMTA1NmJhMGM5YzhmMTA2MjExMzIzZGFhMWY1ZTM0MWIyZGJkN2E2NWZhZjQyYjRhNzE1ZjU2Mzk4NmU4Y2E5OWl1eDRPS3poQ3lUN1pBUG03NTNRdytZSGkxdHlEZVVacGV4MVkxTEhqQTJ2cEtDcEE0Q3ZpUUh0MGM3aVpYeDdFVXZBUXNXOStjWHVtcjBiMHQxUT09",
        'cc_attribution': '“Frozen brush” by Jason Labbehttp://openprocessing.org/sketch/413567License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0',
        'visual_complexity': Level.LOW,
        'visual_contrast': Level.HIGH
    },
    {
        "title": "Black & white tiles",
        "url": "https://openprocessing.org/sketch/1802452/embed/?plusEmbedHash=MzYxYzA1YWExOGJkZDU0OWRlZTAxNDU4ODA4ODM1ZGVjZmMwZGI2NTNjNjViZTRlZDA2OWVhNTJmZmE4YWFlMGNjYzFkYThjNzI1MTA2ZmViYjY3YjdiNjhmMjk0ODg5MzY5MjczYTEzOTM3ZTE4YzVhYjg0NDAwZjhhMTQ0NjBMTnl0cmMvQ24wdWh2a1JEWW5KQkwvbEpoejVjN3I0WXdsY2tqb2NIdHlGNlZPcWJuTng1bDN1UXBYdy9pMHEwY0E0QmZBc3JlV3dtN3lmZTFrS1Zqdz09",
        "cc_attribution": "Black & white tiles by Prakhar Adityahttp://openprocessing.org/sketch/1802452License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.HIGH,
    },
    {
        "title": "Interactive Blob",
        "url": "https://openprocessing.org/sketch/1555443/embed/?plusEmbedHash=YjFkNmMwYTQ3NDE3OWIxZTQ0MmY1NjI2Yzc4YTE1NGEzOTNiODEwYWVmMmY3NmRkNDNjYjJiNDFiNjAwYmVhZjlmZTIwZDQwMDU1MDc3M2NjNTIzMWZhOTY0Y2VkOGY0OTEyNjRlYTZkNzA2NTVhMzY3Njc2NWJiYjZlYjExMDJsbGZHZXVKVWN0ZlZUTWUrOGNyQnRGUTVKbHY3TFM1d01TMlpjdTBIQTBVTDJTaWxVS1N6QnRPbVVoUTBoU2lJc0RVUzZEMlFYMWEvb3lLazBYOW56UT09",
        "cc_attribution": "“Interactive Blob” by Juhani Halkomäkihttp://openprocessing.org/sketch/1555443License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.HIGH,
    },
    {
        "title": "Descendance 6",
        "url": "https://openprocessing.org/sketch/1744394/embed/?plusEmbedHash=Y2ZkYjdmMWQ2YjZlYmM2NWY3ZDY4ODY1ZDhmODAzODI0YTk5M2I0ZjNhZWM3ZjE3ZGEyZTMwNDVmMDhmMmVhZjhjMmYxNzQ2OTIwZjI5YjBmOWZjZWM3NmM2MWMyMDk0NzJkZTg0OGUyYzM3Mzc1ZWU5NmViYjRjYmFmN2FhZmQ2aWt2cExvZ0tyYjBoSUgzNmJHZVp6Q1BONlpLV0RwZlBvcTZzbFhWdXJLRWlpT0hkTWhkVWNYSlBoNnpOamU5UlFRUDlTM2Q3OS9iK1JtZlhzNTJMZz09",
        "cc_attribution": "“Descendance 6 [Sound Sequencer]” by Vamosshttp://openprocessing.org/sketch/1744394License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.LOW
    },
    {
        "title": "Wandering Particles ",
        "url": "https://openprocessing.org/sketch/880007/embed/?plusEmbedHash=ZGIzMDZiZDg2ZGZmNDllMGE1OWRhZTYyNjM1NDAxNzY3ODIxOWQxNjkyMDIxZDE0M2U1ZjM4OWZkNjIwNzJlN2I0NjZmZTBhYTMwNDYyYWFhZjk2ZGFhOWE3YWM1NWQyYjg1YjljZGY2MWFkNDAzNGMzODY4MzVlOWNmMTNjOTd2YnNrdUEvY1ZTcjVyZ0JKNWZ0dXIxb1c1dlRKOVQvMXJ2T3dvc3lzZTc0dzluelIrY1c3VFVYTzNKUkdWVEdyWVRjLzM0WlJxZGhjbFcrV3RQbXd0dz09",
        "cc_attribution": "“Wandering (trailing)Particles” by porthttp://openprocessing.org/sketch/880007License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.HIGH,  
        },
    {
        "title": "0133909",
        "url": "https://openprocessing.org/sketch/972554/embed/?plusEmbedHash=YmYxZjU0ZjhhYzQ1MjI5NzI1NGI0ZDE5N2Q3OTU1NGMzNWJjMTE3M2JiZWJhNTUxNDYwZDVkYzYwMDhmNWRhMTNlYTZlMTYyN2MwYWEzZDk4OGJkZTc0MjBlZjZkZDNmM2MxNzE2NGJiNjg0OGU4MDQ1N2I5ZWEzMjIzOTRhNmVhNThYZTRkOTFCWmkrb2dJb0N5ZHU3TE4xdmVYRStvcEwrU29JWDdOV3BGNDNKSUZIZWFvMm1seWJ4akpiajN4K2lFS2lWT04yY1VSN1lGY2FGb2FWQT09",
        "cc_attribution": "“0133909” by Luis Ruizhttp://openprocessing.org/sketch/972554License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.MEDIUM,
    },
    {
        "title": "The Blue Moon",
        "url": "https://openprocessing.org/sketch/1300372/embed/?plusEmbedHash=ZjQ5Njc3MWJjZjNmODY1ZmQ4OTIzNTJiN2U2YmEyODY5MmI1NmZkZjJjMWMzNmY4Y2VkM2I0MTM2ODk4MzRiYmM5NzllMmI2YjhlZDVlOWRjYmQyNmM5MzFlZWE4NTc4MzlkODljOTczMWU5MzAyZTIzZjMwNmY0NDZmODM4NzIxWVZwVkVhNnNWOHVsMnNmdHhHWllHOTdkVm5qQy9xVmFQWnkycGxMMmRrOWZVbjUyeXV2VEpReWdQdHlxV1k0TmhjVCtnRkZlalRONSsySUg5alNoQT09",
        "cc_attribution": "“The Blue Moon - Pixies Involved” by Eleciahttp://openprocessing.org/sketch/1300372License CreativeCommons Attribution ShareAlikehttps://creativecommons.org/licenses/by-sa/3.0",
        "visual_complexity": Level.LOW,
        "visual_contrast": Level.HIGH,  
        },
    {
        "title": "drip",
        "url": "https://openprocessing.org/sketch/1247449/embed/?plusEmbedHash=OGRiMjhhODEwYThjNGVlYTc5N2M2ZGI3Y2FiYTU2NzFmYjFjZTI2ODkwYzhlMjk1NDM4MzEyM2RlMWZlMGU1NDk0MGI3NDcyNWRlYzRkNDVjMmZhMjY4YWNkZmVmNDZjMDM1ZDEyMDYwZmJmMzBjMjczMjZlYjNkZWEzZWJhZTB0aFFOZ2RVcTQ3NUovd3ROSkVlaUY5L3dYSGFzYXQyVlJzV0JYcHhJbTdTeTJQcThRWDBIYjJXMnI5OVQ1NUtCMjZpaGVpMVA2Y1FkMDN3QTNSOWRFdz09",
        "cc_attribution": "“drip” by Aaron Reuland (a_ soluble_fish)http://openprocessing.org/sketch/1247449License CreativeCommons Attribution NonCommercial ShareAlikehttps://creativecommons.org/licenses/by-nc-sa/3.0",
        "visual_complexity": Level.HIGH,
        "visual_contrast": Level.LOW
    },
    {
        "title": "200417",
        "url": "https://openprocessing.org/sketch/875086/embed/?plusEmbedHash=ZjIxOTFkMDY2ODY2MmZhZmFiZmFiZmMxZjczZjk4ZDdjMmQ0Yzc3NmFmNzc1YTlmZTM4ZGU1ZDIzMTMwYTFlY2MzMmU5YjMxYmQ3N2IzM2IxZTg5N2Y5Yzc5YTE4M2RjZjc0ODBjYzhlZmE5M2YxODUyZjkzYjFjYzVmMDZhYWVGaG1mOXVaclVoeXEyWEtuK3ZZN0dYZ0g4MVFHQzNVMURkeGhYNi9JTm8zVVNkT2xqZkg0c1k0WUZHLzVuMExxVmpyRDF1c0JQV1pNQ3hNazFpL3R2Zz09",
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
