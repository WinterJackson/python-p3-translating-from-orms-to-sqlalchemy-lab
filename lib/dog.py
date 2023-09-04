from models import Dog
from sqlalchemy import create_engine
import os


def create_table(base, engine):
    base.metadata.create_all(engine)
    engine.dispose()


def save(session, dog):
    session.add(dog)
    session.commit()
    session.close()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()


def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()


def update_breed(session, dog, breed):
    dogUpdate = session.query(Dog).filter(Dog.name == dog.name).first()
    dogUpdate.breed = breed
    session.commit()
    session.close()