# seed.py
from app import app
from models import db, Bird

with app.app_context():
    print('Deleting existing birds...')
    Bird.query.delete()

    print('Creating bird objects...')
    birds = [
        Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus'),
        Bird(name='Grackle', species='Quiscalus Quiscula'),
        Bird(name='Common Starling', species='Sturnus Vulgaris'),
        Bird(name='Mourning Dove', species='Zenaida Macroura')
    ]

    db.session.add_all(birds)
    db.session.commit()
    print('Seed complete!')
